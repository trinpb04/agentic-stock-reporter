import os
import time
from google import genai
from google.genai import types
from src.agents.schemas import MarketModel

def run_analyzer_agent(raw_news_data: str, market: str = "VN") -> MarketModel:
    # 1. Khởi tạo Client với SDK google-genai mới nhất
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    
    # 2. Thiết lập System Instruction (Định hình tư duy Agent)
    system_instruction = (
        "Bạn là một Chuyên gia Phân tích Phòng Nghiên cứu của Công ty Chứng khoán. "
        "Nhiệm vụ của bạn là đọc toàn bộ tin tức thô được cung cấp, lọc bỏ tin rác, "
        "và trích xuất dữ liệu chính xác vào cấu trúc JSON được yêu cầu."
    )
    
    # 3. Gọi Gemini với cơ chế Ép dữ liệu đầu ra (Structured Output)
    prompt = f"Hãy phân tích đống dữ liệu thô sau đây của thị trường {market}:\n\n{raw_news_data}"
    
    max_retries = 5
    for attempt in range(max_retries):
        try:
            # Loại bỏ dấu ngoặc kép thừa (nếu set bằng CMD) và dùng bản 1.5-flash siêu nhẹ
            selected_model = os.environ.get("GEMINI_MODEL", "gemini-1.5-flash").strip('"\'')
            response = client.models.generate_content(
                model=selected_model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    # Đây chính là Mechanic ép AI trả về đúng model mẫu
                    response_mime_type="application/json",
                    response_schema=MarketModel,
                    temperature=0.2, # Giảm sáng tạo để tăng độ chính xác của số liệu
                ),
            )
            return response.text
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            print(f"   ⏳ API đang quá tải (lần thử {attempt + 1}/{max_retries}). Đợi 10 giây trước khi thử lại...")
            time.sleep(10)
