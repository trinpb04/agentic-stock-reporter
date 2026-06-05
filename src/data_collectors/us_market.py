import requests
from bs4 import BeautifulSoup
import yfinance as yf

def fetch_us_market_data() -> dict:
    print("🌐 Đang thu thập dữ liệu thực tế từ thị trường Mỹ (S&P 500)...")
    data_output = {"news": [], "top_stocks": []}
    
    # 1. Lấy dữ liệu điểm số của chỉ số S&P 500 (^GSPC) qua yfinance
    try:
        sp500 = yf.Ticker("^GSPC")
        hist = sp500.history(period="1d")
        if not hist.empty:
            close_price = round(hist['Close'].iloc[0], 2)
            open_price = round(hist['Open'].iloc[0], 2)
            pct_change = round(((close_price - open_price) / open_price) * 100, 2)
            sign = "+" if pct_change >= 0 else ""
            data_output["news"].append(
                f"Chỉ số S&P 500 đóng cửa ở mức {close_price} điểm (Biến động: {sign}{pct_change}%)."
            )
    except Exception as e:
        print(f"⚠️ Lỗi khi lấy dữ liệu yfinance: {e}")

    # 2. Cào tin tức tài chính quốc tế từ RSS của Yahoo Finance
    try:
        rss_url = "https://finance.yahoo.com/news/rssindex"
        response = requests.get(rss_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        soup = BeautifulSoup(response.content, features="xml")
        items = soup.find_all("item")
        
        # Lấy 5 tiêu đề tin tức quốc tế mới nhất
        for item in items[:5]:
            title = item.title.text.strip()
            description = item.description.text.strip() if item.description else ""
            data_output["news"].append(f"{title}: {description}")
    except Exception as e:
        print(f"⚠️ Lỗi khi cào RSS Yahoo Finance: {e}")

    # 3. Định nghĩa các mã cổ phiếu công nghệ lớn (Magnificent Seven) đáng chú ý
    # Trong môi trường production thực tế, người dùng có thể tự cấu hình danh sách này
    data_output["top_stocks"] = [
        {"ticker": "NVDA", "event": "NVIDIA tiếp tục dẫn dắt làn sóng AI phần cứng, vốn hóa chạm mốc kỷ lục mới nhờ nhu cầu chip Blackwell tăng mạnh."},
        {"ticker": "AAPL", "event": "Apple công bố các tính năng AI mới tích hợp sâu vào hệ điều hành, kích thích chu kỳ nâng cấp thiết bị của người dùng."},
        {"ticker": "TSLA", "event": "Cổ phiếu biến động mạnh trước các thông tin về tiến độ cấp phép phần mềm tự lái FSD tại các thị trường quốc tế."}
    ]
    
    return data_output
