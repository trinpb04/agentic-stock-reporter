# Agentic Stock Reporter 🚀

Hệ thống AI tự động thu thập tin tức, phân tích thị trường chứng khoán và xuất bản báo cáo (Markdown) hàng ngày.

## 🌟 Tính năng nổi bật
1. **Cào dữ liệu (Collector)**: Tự động trích xuất tin tức RSS từ CafeF và top các mã cổ phiếu nổi bật.
2. **Ép khuôn (Analyzer)**: Sử dụng Gemini để phân tích văn bản thô và cấu trúc hóa dữ liệu (Structured Outputs) vào định dạng JSON cố định.
3. **Biên tập viên (Writer)**: Dùng Gemini biến dữ liệu JSON khô khan thành một bản báo cáo Markdown sắc sảo, chuyên nghiệp.
4. **Tự động hóa (Automation)**: Tích hợp sẵn GitHub Actions để tự động chạy hàng ngày.

## 🛠️ Hướng dẫn cài đặt

### 1. Cài đặt thư viện
```bash
pip install -r requirements.txt
```
*(Nếu chưa có file `requirements.txt`, hãy chạy: `pip install google-genai pydantic requests beautifulsoup4 lxml pandas`)*

### 2. Cấu hình Model AI (Gemini)
Hiện tại, ứng dụng đã được thiết lập mặc định chạy model **`gemini-3.5-flash`** cho siêu tốc độ và thông minh nhất ở môi trường máy tính của bạn (Local).

Để đổi sang một model khác (Ví dụ bạn muốn tiết kiệm chi phí khi đưa lên server hoặc dùng thử `gemini-1.5-pro`), bạn có thể đặt biến môi trường:
- **Windows (CMD)**: `set GEMINI_MODEL="gemini-2.5-flash"`
- **Windows (PowerShell)**: `$env:GEMINI_MODEL="gemini-2.5-flash"`
- **Linux/Mac**: `export GEMINI_MODEL="gemini-2.5-flash"`

### 3. Cấu hình GitHub Actions
Khi đẩy code này lên GitHub, bạn cần tạo khóa bảo mật (Secret):
1. Vào mục **Settings > Secrets and variables > Actions**.
2. Thêm một Secret có tên **`GEMINI_API_KEY`** và dán API Key của bạn vào.
3. (Tùy chọn) Thêm một Secret hoặc Variable tên **`GEMINI_MODEL`** nếu bạn không muốn dùng mặc định `gemini-3.5-flash` trên GitHub.

## 🗂 Cấu trúc thư mục (Lưu ý)
Thư mục `scr` (cũ) đã được đổi tên thành `project_docs` để tránh gây nhầm lẫn với thư mục mã nguồn chính `src`. Bạn có thể tìm thấy các tài liệu cũ bên trong thư mục `project_docs`.
