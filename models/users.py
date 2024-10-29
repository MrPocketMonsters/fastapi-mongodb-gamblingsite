from pydantic import BaseModel

class BetHistoryItem(BaseModel):
    event: str
    bet: str
    amount: float

class User(BaseModel):
    first_name: str
    last_name: str
    balance: float
    bet_history: list[BetHistoryItem] = []
