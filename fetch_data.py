import yfinance as yf
import json

def fetch_stock_data():
    # Fetch Apple stock data
    ticker = yf.Ticker("AAPL")
    # Get historical market data for 1 month
    hist = ticker.history(period="1mo")
    
    # Convert dataframe to dictionary
    data_dict = hist.reset_index().to_dict(orient='records')
    
    # Convert Timestamp objects to string for JSON serialization
    for row in data_dict:
        if 'Date' in row:
            row['Date'] = row['Date'].isoformat()
            
    # Save to JSON file
    with open('raw_data.json', 'w') as f:
        json.dump(data_dict, f, indent=4)
        
if __name__ == "__main__":
    fetch_stock_data()
    print("Data saved to raw_data.json")
