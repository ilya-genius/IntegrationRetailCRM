from fastapi import APIRouter, status

from app.models.payment import RequestPayment, ResponsePayment
from app.services.payment_service import PaymentService
from app.utils.utils import prepare_payment_payload


payment_router = APIRouter(prefix="/payment", tags=["Платежи"])

service = PaymentService()


@payment_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_payment(input_data: RequestPayment) -> ResponsePayment:
    payload = prepare_payment_payload(input_data)
    return await service.create_payment(payload)
