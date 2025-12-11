from app.clients.retailcrm import RetailCRMClient
from app.models.customers import ResponseCustomer, ResponseAllCustomers


class CustomersService:
    def __init__(self):
        self.client = RetailCRMClient()

    async def fetch_customers(self, filters: dict) -> ResponseAllCustomers:
        data = await self.client.get_customers(filters=filters)
        return ResponseAllCustomers(**data)

    async def add_customer(self, input_data: dict) -> ResponseCustomer:
        output_data = await self.client.add_customer(input_data)
        return ResponseCustomer(**output_data)
