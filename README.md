<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=timeGradient&height=200&section=header&text=Agentic%20Stock%20Reporter&fontSize=50&fontAlignY=38&desc=Autonomous%20AI%20Financial%20Analyst&descAlignY=51&descAlign=62&animation=twinkling" />
</p>

<p align="center">
  <a href="#"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=20&pause=1000&color=2799FF&center=true&vCenter=true&width=435&lines=Human-AI+Co-coding+Architecture;Zero-cost+Automated+Market+Reports;Multi-market:+VNIndex+%26+S%26P+500" alt="Typing SVG" /></a>
</p>

---

## 🤖 Introduction

**Agentic Stock Reporter** là một hệ thống AI Agent tự chủ, tối ưu chi phí (Zero-Cost) chuyên tự động hóa quy trình tổng hợp, phân tích và xuất bản báo cáo thị trường chứng khoán (Việt Nam & Mỹ S&P 500) hàng ngày. 

Dự án này là sản phẩm của mô hình làm việc **Human-AI Co-coding**: 
- 🧠 **Ý tưởng thiết kế, Kiến trúc hệ thống & Giám sát chất lượng:** Khởi xướng và tinh chỉnh bởi Con người (Product Owner).
- 💻 **Thực thi, Lập trình & Sửa lỗi (Self-correction):** Triển khai bởi AI thông qua môi trường phát triển Google Antigravity.

*(Scroll down for English setup instructions)*

---

## ✨ Tính năng cốt lõi (Key Features)

* 🌐 **Thu thập dữ liệu đa thị trường (Multi-market):** Tự động cào tin tức vĩ mô và dữ liệu kỹ thuật từ các nguồn trực tuyến tin cậy cho cả thị trường Việt Nam (CafeF RSS) và Mỹ (Yahoo Finance & `yfinance`).
* 🧩 **Bộ não Agent trích xuất cấu trúc (Strict Schema Extraction):** Sử dụng tính năng *Structured Outputs* của `gemini-1.5-flash` và `gemini-2.5-flash` để ép dữ liệu thô lộn xộn vào khuôn mẫu `Pydantic JSON` chuẩn xác 100%, loại bỏ hoàn toàn hiện tượng AI trả lời lan man.
* ✍️ **Biên tập báo cáo tự động (AI Writer Agent):** Chuyển đổi dữ liệu JSON khô khan thành một bản báo cáo tài chính bằng ngôn ngữ Markdown sắc sảo, văn phong chuyên nghiệp.
* 🔔 **Cổng phát ngôn Discord (Discord Push Notification):** Tích hợp hệ thống tự động chia nhỏ tin nhắn (Chunking) để bắn báo cáo trực tiếp về kênh Discord cá nhân, giúp cập nhật thông tin mọi lúc mọi nơi trên điện thoại.
* ☁️ **Tự động hóa hoàn toàn (CI/CD Automation):** Cấu hình chạy tự động vào 17:15 hàng ngày sau giờ đóng cửa thông qua GitHub Actions mà không tốn một đồng chi phí vận hành máy chủ.

---

## 📖 Getting Started (Local Setup)

Follow these steps to clone the code and run it on your own machine.

### Step 1: Clone the repository
Open your Terminal (or CMD/PowerShell on Windows) and run the following command to download the code:
```bash
git clone https://github.com/YOUR_USERNAME/agentic-stock-reporter.git
cd agentic-stock-reporter
```

### Step 2: Install dependencies
Make sure you have Python installed (version 3.10 or higher). Run the following command to install the required libraries:
```bash
pip install -r requirements.txt
```

### Step 3: Set up your Discord Webhook
To receive reports on Discord, you need a Webhook URL:
1. Open Discord and go to your Server.
2. Create or select a text channel (e.g., `#market-reports`).
3. Click the **Edit Channel** gear icon next to the channel name.
4. Go to **Integrations** -> **Webhooks** -> **New Webhook**.
5. Name your bot and click **Copy Webhook URL**.

### Step 4: Get your Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/) and sign in with your Google account.
2. Click on **Get API key** and create a new key (It's free).

### Step 5: Configure Environment Variables
Pass these two keys to your computer so the code can use them:

**On Windows (CMD):**
```cmd
set GEMINI_API_KEY="Your_Gemini_API_Key"
set DISCORD_WEBHOOK_URL="Your_Discord_Webhook_URL"
```
**On Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="Your_Gemini_API_Key"
$env:DISCORD_WEBHOOK_URL="Your_Discord_Webhook_URL"
```
**On Mac/Linux:**
```bash
export GEMINI_API_KEY="Your_Gemini_API_Key"
export DISCORD_WEBHOOK_URL="Your_Discord_Webhook_URL"
```

### Step 6: Run the AI Agent
Start the data collection and report generation:

- Analyze the **Vietnam Market (Default)**:
  ```bash
  python -m src.main
  ```
- Analyze the **US Market (S&P 500)**:
  ```bash
  python -m src.main --market US
  ```

*Tada! Check your Discord channel to see the result. The markdown report will also be saved locally in the `reports/` folder.*

---

## 🤖 Automating with GitHub Actions

You don't want to run the command manually every day? Let GitHub do it for you automatically!

1. Push this project to your own GitHub Repository.
2. Go to your GitHub Repository page.
3. Click on the **Settings** tab at the top.
4. In the left sidebar, scroll down and click on **Secrets and variables**, then select **Actions**.
5. Click the green **New repository secret** button.
6. Add the following secrets:
   - Name: `GEMINI_API_KEY` | Secret: *Paste your Gemini API Key*
   - Name: `DISCORD_WEBHOOK_URL` | Secret: *Paste your Discord Webhook URL*
7. **That's it!** The workflow is already configured. Every weekday (Monday to Friday) at 10:15 UTC, GitHub Actions will run the AI Agent and send the results to your Discord channel.

---

## ⚖️ License
This project is licensed under the **MIT License**. You are free to use, modify, and distribute it. See the `LICENSE` file for more details.

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=timeGradient&height=100&section=footer" />
</p>
