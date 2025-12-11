from fastapi import APIRouter, Depends, status

from app.services.orders_service import OrdersService
from app.models.orders import RequestOrder, ResponseOrderFull, RequestAllOrders, ResponseAllOrders
from app.utils.utils import prepare_order_payload, prepare_orders_all_payload

order_router = APIRouter(prefix="/orders", tags=["Заказы"])

service = OrdersService()

@order_router.get("/")
async def get_orders(params: RequestAllOrders = Depends()) -> ResponseAllOrders:
    filters = prepare_orders_all_payload(params)
    return await service.fetch_orders(filters=filters)

@order_router.post("/", status_code=status.HTTP_201_CREATED)
async def add_order(input_data: RequestOrder) -> ResponseOrderFull:
    payload = prepare_order_payload(input_data)
    return await service.add_order(payload)


