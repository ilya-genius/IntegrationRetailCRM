from app.clients.retailcrm import RetailCRMClient
from app.models.orders import ResponseOrderFull, ResponseAllOrders


class OrdersService:
    def __init__(self):
        self.client = RetailCRMClient()

    async def fetch_orders(self, filters: dict) -> ResponseAllOrders:
        data = await self.client.get_orders(filters=filters)
        return ResponseAllOrders(**data)

    async def add_order(self, input_data: dict) -> ResponseOrderFull:
        output_data = await self.client.add_order(input_data)
        return ResponseOrderFull(**output_data)

