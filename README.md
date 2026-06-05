# 🚀 Agentic Stock Reporter

**Agentic Stock Reporter** is an open-source AI Agent system capable of automatically scraping stock market data, analyzing it, and generating professional daily reports. It supports multi-market data (Vietnam & US) and automatically sends the report directly to your Discord channel via push notifications.

This project is designed to be extremely easy to use, making it suitable for both programming beginners and AI enthusiasts.

---

## ✨ Features
- 🌐 **Multi-market Support**: Fetches stock data for the Vietnam market (VNIndex, CafeF) and the US market (S&P 500, Yahoo Finance).
- 🧠 **Agentic AI Brain**: Utilizes Google's `gemini-1.5-flash` and `gemini-2.5-flash` to analyze raw text, extract structured data (JSON), and write comprehensive markdown reports.
- 💬 **Discord Webhook Integration**: Features smart message chunking to bypass Discord's 2000-character limit, pushing full reports directly to your phone or computer.
- ⚡ **100% Automated**: Comes with a pre-configured GitHub Actions workflow. You don't need to leave your computer on; GitHub will run the agent automatically every day at 10:15 AM UTC (5:15 PM GMT+7) for free.

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
4. Go to **Integrations** $\rightarrow$ **Webhooks** $\rightarrow$ **New Webhook**.
5. Name your bot (e.g., "Agentic Stock Reporter") and click **Copy Webhook URL**.

### Step 4: Get your Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/) and sign in with your Google account.
2. Click on **Get API key** and create a new key (It's free).

### Step 5: Configure Environment Variables
You need to pass these two keys to your computer so the code can use them. Run the corresponding commands in your terminal:

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
Now, run the following command to start the data collection and report generation:

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
6. Create the first secret:
   - **Name**: `GEMINI_API_KEY`
   - **Secret**: *Paste your Gemini API Key here*
   - Click **Add secret**.
7. Create the second secret:
   - **Name**: `DISCORD_WEBHOOK_URL`
   - **Secret**: *Paste your Discord Webhook URL here*
   - Click **Add secret**.

**That's it!** The workflow is already configured in the `.github/workflows/daily_market_report.yml` file. From now on, every weekday (Monday to Friday) at 10:15 UTC, GitHub Actions will spin up a server, run the AI Agent, commit the new report back to the repository, and send the results to your Discord channel.

*(Note: The workflow uses `gemini-2.5-flash` by default. If you want to use a different model, you can add a third secret named `GEMINI_MODEL` and set its value to your preferred model, like `gemini-1.5-flash`).*

---

## ⚖️ License
This project is licensed under the **MIT License**. You are free to use, modify, and distribute it. See the `LICENSE` file for more details.
