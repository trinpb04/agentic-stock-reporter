<p align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />
</p>

<h1 align="center">🤖 Agentic Stock Reporter</h1>

<p align="center">
  <a href="#"><img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=20&pause=1000&color=2799FF&center=true&vCenter=true&width=435&lines=Human-AI+Co-coding+Architecture;Zero-cost+Automated+Market+Reports;Multi-market:+VNIndex+%26+S%26P+500" alt="Typing SVG" /></a>
</p>

## 🤖 Introduction

**Agentic Stock Reporter** is an autonomous, zero-cost AI Agent system designed to automate the process of aggregating, analyzing, and publishing daily stock market reports (covering Vietnam & US S&P 500).

This project is the result of a **Human-AI Co-coding** workflow:
- 🧠 **Design, Architecture & Quality Assurance:** Initiated and refined by a Human (Product Owner).
- 💻 **Execution, Coding & Self-correction:** Implemented entirely by AI.

---

## ✨ Key Features

* 🌐 **Multi-market Data Collection:** Automatically scrapes macroeconomic news and technical data from reliable online sources for both the Vietnam market (CafeF RSS) and the US market (Yahoo Finance & `yfinance`).
* 🧩 **Strict Schema Extraction:** Utilizes the *Structured Outputs* capability of `gemini-1.5-flash` and `gemini-2.5-flash` to parse messy raw data into a strict 100% accurate `Pydantic JSON` format, eliminating AI hallucinations.
* ✍️ **AI Writer Agent:** Transforms dry JSON data into a sharp, professionally-toned financial report using Markdown syntax.
* 🔔 **Discord Push Notification:** Features an intelligent message chunking system to bypass Discord API limits, delivering real-time market insights directly to your personal Discord channel.
* ☁️ **100% CI/CD Automation:** Pre-configured with GitHub Actions to run automatically every weekday, costing absolutely zero dollars in server hosting.

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
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" />
</p>
