from pydantic import BaseModel, Field
from typing import List

class MarketSentiment(BaseModel):
    status: str = Field(description="Xu hướng chung: Tích cực, Tiêu cực, hoặc Đi ngang")
    score: int = Field(description="Điểm số tâm lý từ 1 đến 10")
    reason: str = Field(description="Lý do ngắn gọn dẫn đến tâm lý này")

class StockHighlight(BaseModel):
    ticker: str = Field(description="Mã cổ phiếu (Ví dụ: VCB, HPG)")
    event: str = Field(description="Sự kiện hoặc biến động đáng chú ý trong ngày của mã này")

class MarketModel(BaseModel):
    market_name: str = Field(description="Tên thị trường (VNIndex hoặc S&P500)")
    sentiment: MarketSentiment
    top_news_summary: List[str] = Field(description="Tóm tắt 3-5 tin tức vĩ mô quan trọng nhất ảnh hưởng thị trường")
    watched_stocks: List[StockHighlight] = Field(description="Danh sách các cổ phiếu cần chú ý đặc biệt")
