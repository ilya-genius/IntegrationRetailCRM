from fastapi import APIRouter, Depends, status

from app.models.customers import RequestCustomer, ResponseCustomer, ResponseAllCustomers, RequestAllCustomers
from app.services.customers_service import CustomersService
from app.utils.utils import prepare_retailcrm_payload, prepare_customers_all_payload

customer_router = APIRouter(prefix="/customers", tags=["Клиенты"])

service = CustomersService()

@customer_router.get("/")
async def get_customers(params: RequestAllCustomers = Depends()) -> ResponseAllCustomers:
    filters = prepare_customers_all_payload(params)
    return await service.fetch_customers(filters=filters)

@customer_router.post("/", status_code=status.HTTP_201_CREATED, response_model=ResponseCustomer)
async def add_customer(input_data: RequestCustomer) -> ResponseCustomer:
    payload = prepare_retailcrm_payload(input_data)
    return await service.add_customer(payload)

