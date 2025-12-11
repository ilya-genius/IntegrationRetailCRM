from app.clients.retailcrm import RetailCRMClient
from app.models.payment import ResponsePayment


class PaymentService:
    def __init__(self):
        self.client = RetailCRMClient()

    async def create_payment(self, input_data: dict) -> ResponsePayment:
        output_data = await self.client.create_payment(input_data)
        return ResponsePayment(**output_data)
