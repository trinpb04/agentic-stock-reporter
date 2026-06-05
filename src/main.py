import os
import json
import argparse
from datetime import datetime
from src.data_collectors.vn_market import fetch_vn_market_data
from src.data_collectors.us_market import fetch_us_market_data
from src.agents.analyzer_agent import run_analyzer_agent
from src.agents.writer_agent import run_writer_agent
from src.utils.discord_notifier import send_discord_report

def main():
    # Cấu hình bộ nhận tham số dòng lệnh (CLI Arguments) để người khác dễ dùng
    parser = argparse.ArgumentParser(description="Agentic Stock Reporter - Bộ tạo báo cáo chứng khoán tự động bằng AI.")
    parser.add_argument(
        "--market", 
        type=str, 
        default="VN", 
        choices=["VN", "US"], 
        help="Chọn thị trường cần phân tích: VN (Việt Nam) hoặc US (Mỹ). Mặc định là VN."
    )
    args = parser.parse_args()
    
    market = args.market.upper()
    print(f"🚀 Khởi động Agentic Stock Reporter cho thị trường: {market}...")
    
    # 1. Lựa chọn bộ Collector tương ứng với tham số truyền vào
    if market == "VN":
        raw_market_dict = fetch_vn_market_data()
    elif market == "US":
        raw_market_dict = fetch_us_market_data()
    else:
        print("❌ Thị trường không hợp lệ.")
        return
        
    raw_content = json.dumps(raw_market_dict, ensure_ascii=False)

    # 2. Phân tích dữ liệu (AI Agent 1)
    print("🤖 AI Agent 1: Đang phân tích và cấu trúc hóa dữ liệu...")
    structured_json = run_analyzer_agent(raw_content, market=market)
    
    # 3. Biên tập báo cáo bằng tiếng Việt (AI Agent 2)
    print("✍️ AI Agent 2: Đang dịch thuật và biên tập báo cáo thành văn bản...")
    final_report = run_writer_agent(structured_json, market=market)
    
    # 4. Lưu file báo cáo cục bộ
    os.makedirs("reports", exist_ok=True)
    today_str = datetime.now().strftime("%Y-%m-%d")
    report_filename = f"reports/market_report_{market}_{today_str}.md"
    with open(report_filename, "w", encoding="utf-8") as f:
        f.write(final_report)
    print(f"🎉 Đã xuất bản báo cáo cục bộ tại: {report_filename}")

    # 5. Gửi thông báo đến cổng Discord (nếu có cấu hình)
    send_discord_report(final_report)

if __name__ == "__main__":
    main()
