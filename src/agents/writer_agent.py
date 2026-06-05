import os
import time
from google import genai
from google.genai import types

def run_writer_agent(structured_json_data: str, market: str = "VN") -> str:
    """
    Agent này chịu trách nhiệm chuyển đổi dữ liệu JSON đã phân tích thành
    một bài báo cáo chỉn chu bằng định dạng Markdown.
    """
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    
    system_instruction = (
        "Bạn là một Biên tập viên cao cấp của một tạp chí tài chính danh tiếng. "
        "Nhiệm vụ của bạn là tiếp nhận dữ liệu cấu trúc (JSON) về thị trường chứng khoán, "
        "sau đó viết thành một bản báo cáo thị trường hàng ngày bằng định dạng Markdown (.md). "
        "Bản báo cáo cần có tiêu đề rõ ràng, sử dụng các ký hiệu Bullet points, Bảng biểu (nếu cần) "
        "để người đọc dễ nắm bắt thông tin nhất. Văn phong chuyên nghiệp, sắc sảo, khách quan."
    )
    
    prompt = (
        f"Dưới đây là dữ liệu cấu trúc của thị trường {market} ngày hôm nay:\n\n"
        f"{structured_json_data}\n\n"
        f"Hãy viết một bản báo cáo hoàn chỉnh bằng tiếng Việt dựa trên dữ liệu này. "
        f"Lưu ý: Chỉ trả về nội dung Markdown chính thức, không kèm theo lời thoại của AI ở đầu hoặc cuối."
    )
    
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
                    temperature=0.7, # Tăng một chút sáng tạo để văn phong mượt mà, tự nhiên hơn
                ),
            )
            return response.text
        except Exception as e:
            if attempt == max_retries - 1:
                raise e
            print(f"   ⏳ API đang quá tải (lần thử {attempt + 1}/{max_retries}). Đợi 10 giây trước khi thử lại...")
            time.sleep(10)
