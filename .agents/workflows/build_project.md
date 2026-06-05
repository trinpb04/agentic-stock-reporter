# Workflow: Project Development Roadmap

## Phase 1: Initialize Project & Setup Data Collector (Vietnam Market First)
- **Goal:** Create repository structure, configure requirements.txt, and write the first data collector.
- **Tasks:**
  1. Initialize `requirements.txt` with `google-genai`, `vnstock`, `pandas`, `requests`, and `beautifulsoup4`.
  2. Create `src/data_collectors/vn_market.py` to fetch daily prices (VNIndex) and top market news from financial sites (e.g., CafeF RSS).
  3. Verify the collector works by running it via the integrated terminal and saving a sample `raw_data.json`.

## Phase 2: Design the AI Brain & Agent Modules
- **Goal:** Build the logical thinking layer of the reporter using Gemini.
- **Tasks:**
  1. Create a JSON schema file `src/templates/model_template.json` to define the data structure.
  2. Create `src/agents/analyzer_agent.py` using `google-genai` to parse the raw text/news into the structured JSON schema.
  3. Create `src/agents/writer_agent.py` to ingest the JSON data and compile it into a beautifully formatted Markdown report based on a template.

## Phase 3: Orchestration & Automation
- **Goal:** Connect everything under a single main execution file and automate it.
- **Tasks:**
  1. Write `src/main.py` to orchestrate the entire flow (Fetch -> Analyze -> Write).
  2. Setup `.github/workflows/daily_market_report.yml` to trigger the Python script daily at market close using GitHub Actions.
  3. Ensure it automatically commits the generated report to the GitHub repository.

## Phase 4: Expansion to US Market
- **Goal:** Add support for the US Stock Market (S&P 500 / Nasdaq).
- **Tasks:**
  1. Create `src/data_collectors/us_market.py` utilizing `yfinance` and Yahoo Finance scrapers.
  2. Add a command-line argument `--market` (VN or US) to `src/main.py` to easily toggle between markets.