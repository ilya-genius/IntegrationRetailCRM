from pydantic import BaseModel, Field
from datetime import datetime

class RequestPayment(BaseModel):
    id: int = Field(ge=1)
    amount: float = Field(gt=0)
    paid_at: datetime = Field(default_factory=datetime.now, alias="paidAt")
    type_payment: str = Field(alias="type")


class ResponsePayment(BaseModel):
    success: bool
    id: int
