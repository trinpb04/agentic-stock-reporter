# 🚀 Agentic Stock Reporter

**Agentic Stock Reporter** là một hệ thống Trợ lý Trí tuệ Nhân tạo (AI Agent) mã nguồn mở, có khả năng tự động cào dữ liệu thị trường chứng khoán, phân tích và viết báo cáo chuyên nghiệp mỗi ngày. Hệ thống hỗ trợ đa thị trường (Việt Nam & Mỹ) và tự động bắn thông báo báo cáo thẳng về kênh Discord của bạn.

Dự án này được thiết kế cực kỳ dễ sử dụng, phù hợp cho cả những người mới bắt đầu lập trình hoặc chưa có nhiều kinh nghiệm về AI.

---

## ✨ Tính năng nổi bật
- 🌐 **Đa thị trường (Multi-market)**: Lấy dữ liệu chứng khoán Việt Nam (VNIndex, CafeF) hoặc Mỹ (S&P 500, Yahoo Finance).
- 🧠 **Tư duy AI sắc sảo**: Sử dụng `gemini-1.5-flash` và `gemini-2.5-flash` của Google để dịch thuật, tổng hợp và ép khuôn dữ liệu thành báo cáo hoàn chỉnh.
- 💬 **Tích hợp Discord Webhook**: Chia nhỏ tin nhắn thông minh, bắn thẳng thông báo về điện thoại/máy tính của bạn ngay khi có báo cáo mới.
- ⚡ **Tự động hóa 100%**: Đi kèm sẵn cấu hình GitHub Actions. Bạn không cần treo máy, GitHub sẽ tự động chạy code vào 17:15 chiều mỗi ngày hoàn toàn miễn phí.

---

## 📖 Hướng dẫn Cài đặt & Chạy trên máy tính (Cho người mới)

Dưới đây là các bước để bạn "mang bộ code này về máy" và tự chạy một cách đơn giản nhất.

### Bước 1: Tải mã nguồn về máy (Clone)
Mở Terminal (hoặc CMD/PowerShell trên Windows) và gõ lệnh sau để tải toàn bộ code từ GitHub về máy tính của bạn:
```bash
git clone https://github.com/TEN_DANG_NHAP_CUA_BAN/agentic-stock-reporter.git
cd agentic-stock-reporter
```

### Bước 2: Cài đặt thư viện Python
Đảm bảo máy bạn đã cài sẵn Python (Phiên bản từ 3.10 trở lên). Gõ lệnh sau để cài đặt các "phụ tùng" cần thiết:
```bash
pip install -r requirements.txt
```

### Bước 3: Cấu hình "Chìa khóa" (API Keys)
Để hệ thống hoạt động, AI cần 2 thứ: Chìa khóa bộ não Gemini và Đường dẫn nhận tin nhắn Discord.
* **Cách lấy Gemini API Key**: Truy cập [Google AI Studio](https://aistudio.google.com/), đăng nhập và tạo một API Key (Hoàn toàn miễn phí).
* **Cách lấy Discord Webhook URL**: Vào kênh Discord của bạn $\rightarrow$ Edit Channel $\rightarrow$ Integrations $\rightarrow$ Webhooks $\rightarrow$ Copy Webhook URL.

Gán 2 khóa này vào máy tính của bạn bằng dòng lệnh:
**Trên Windows (CMD):**
```cmd
set GEMINI_API_KEY="Điền API Key của bạn vào đây"
set DISCORD_WEBHOOK_URL="Điền link Webhook Discord của bạn vào đây"
```
**Trên Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="Điền API Key của bạn vào đây"
$env:DISCORD_WEBHOOK_URL="Điền link Webhook Discord của bạn vào đây"
```
**Trên Mac/Linux:**
```bash
export GEMINI_API_KEY="Điền API Key của bạn vào đây"
export DISCORD_WEBHOOK_URL="Điền link Webhook Discord của bạn vào đây"
```

### Bước 4: Khởi chạy AI Agent
Chạy lệnh sau để hệ thống bắt đầu thu thập dữ liệu và xuất báo cáo:

- Phân tích thị trường **Việt Nam (Mặc định)**:
  ```bash
  python -m src.main
  ```
- Phân tích thị trường **Mỹ (S&P 500)**:
  ```bash
  python -m src.main --market US
  ```

*Tada! Mở Discord lên và xem thành quả nhé! File báo cáo cũng sẽ được lưu trực tiếp vào thư mục `reports/` trên máy bạn.*

---

## 🤖 Hướng dẫn cấu hình Tự động hóa (GitHub Actions)

Bạn không muốn ngày nào cũng phải gõ lệnh? Hãy để GitHub tự động làm việc đó thay bạn!

1. Upload (Push) dự án này lên Repository GitHub của bạn.
2. Trên giao diện GitHub của Repo đó, chuyển sang tab **Settings** $\rightarrow$ **Secrets and variables** $\rightarrow$ **Actions**.
3. Bấm **New repository secret** và thêm lần lượt 2 Secret sau:
   - Name: `GEMINI_API_KEY` | Secret: *Dán API Key của bạn vào*
   - Name: `DISCORD_WEBHOOK_URL` | Secret: *Dán Webhook của bạn vào*
4. Xong! Kể từ ngày mai, cứ vào lúc 17:15 chiều (Giờ Việt Nam) từ Thứ 2 đến Thứ 6, GitHub sẽ tự động gọi AI viết báo cáo và gửi vào Discord cho bạn.

*(Mặc định khi đẩy lên GitHub, nó sẽ dùng `gemini-2.5-flash`. Nếu bạn muốn nâng cấp lên mô hình khác, bạn có thể tạo thêm một Secret có tên `GEMINI_MODEL` và điền tên model mong muốn).*

---

## ⚖️ Giấy phép (License)
Dự án được phân phối dưới giấy phép **MIT License**. Bạn hoàn toàn có quyền sử dụng, sửa đổi và phân phối lại thoải mái. Xem chi tiết tại file `LICENSE`.
