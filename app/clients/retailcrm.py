import httpx
from config import settings
from app.core.logging import logger
from fastapi import HTTPException
from app.interfaces.icrm import ICRM


class RetailCRMClient(ICRM):
    def __init__(self):
        self.base_url = settings.RETAILCRM_API_URL
        self.api_key = settings.RETAILCRM_API_KEY
        self.client = httpx.AsyncClient(timeout=10)

    async def __request(self, method: str, endpoint: str, params=None, data=None):
        params = params or {}
        params["apiKey"] = self.api_key

        response = await self.client.request(
            method,
            f"{self.base_url}{endpoint}",
            params=params,
            data=data)

        if not (200 <= response.status_code < 300):
            logger.error(f"Request error, endpoint - {endpoint}, status code = {response.status_code}, error - {response.text}")

            raise HTTPException(
                status_code=response.status_code,
                detail=response.text
            )

        return response.json()

    async def get_customers(self, filters: dict) -> dict:
        return await self.__request("GET", "/api/v5/customers", params=filters)

    async def add_customer(self, input_data: dict) -> dict:
        return await self.__request("POST", "/api/v5/customers/create", data=input_data)

    async def get_orders(self, filters: dict) -> dict:
        return await self.__request("GET", "/api/v5/orders", params=filters)

    async def add_order(self, input_data: dict) -> dict:
        return await self.__request("POST", "/api/v5/orders/create", data=input_data)

    async def create_payment(self, input_data: dict) -> dict:
        return await self.__request("POST", "/api/v5/orders/payments/create", data=input_data)