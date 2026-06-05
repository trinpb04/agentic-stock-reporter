import os
import requests
import time

def send_discord_report(report_text: str):
    """
    Gửi nội dung báo cáo thị trường thẳng vào kênh Discord qua Webhook URL.
    Tự động chia nhỏ tin nhắn nếu vượt quá giới hạn 2000 ký tự của Discord.
    """
    # Loại bỏ dấu ngoặc kép thừa (nếu user set bằng CMD)
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL", "").strip('"\'')
    
    if not webhook_url:
        print("⚠️ Bỏ qua gửi Discord: Chưa cấu hình biến môi trường DISCORD_WEBHOOK_URL.")
        return

    print("📤 Đang gửi báo cáo qua Discord Webhook...")
    
    # Giới hạn an toàn cho tiếng Việt có dấu và định dạng Markdown là 1800 ký tự mỗi tin
    MAX_LENGTH = 1800
    
    # Chia nhỏ văn bản theo từng dòng để tránh việc cắt đôi một từ hoặc một thẻ Markdown
    lines = report_text.split('\n')
    chunks = []
    current_chunk = ""

    for line in lines:
        # Nếu dòng hiện tại + dòng tiếp theo vượt quá giới hạn, đóng chunk hiện tại lại
        if len(current_chunk) + len(line) + 1 > MAX_LENGTH:
            chunks.append(current_chunk.strip())
            current_chunk = line
        else:
            if current_chunk:
                current_chunk += "\n" + line
            else:
                current_chunk = line
                
    # Thêm phần còn lại vào chunk cuối cùng
    if current_chunk:
        chunks.append(current_chunk.strip())

    # Gửi từng chunk lên Discord
    for index, chunk in enumerate(chunks):
        payload = {
            "content": chunk,
            "username": "Agentic Stock Reporter Bot",
            "avatar_url": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=100"
        }

        # Nếu có nhiều hơn 1 chunk, đánh dấu số phần để người đọc dễ theo dõi
        if len(chunks) > 1:
            payload["username"] = f"Agentic Stock Reporter Bot (Phần {index + 1}/{len(chunks)})"

        try:
            response = requests.post(webhook_url, json=payload, timeout=15)
            if response.status_code in [200, 204]:
                print(f"🚀 Đã gửi thành công Phần {index + 1}/{len(chunks)}")
            else:
                print(f"⚠️ Lỗi từ Discord API ở Phần {index + 1}: {response.status_code} - {response.text}")
                
            # Nghỉ 1 giây giữa các lần gửi để tránh bị dính lỗi Rate Limit (gửi quá nhanh) của Discord
            time.sleep(1)
            
        except Exception as e:
            print(f"⚠️ Thất bại khi kết nối tới Discord API: {e}")
