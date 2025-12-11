from abc import ABC, abstractmethod


class ICRM(ABC):

    @abstractmethod
    async def get_customers(self, filters: dict) -> dict:
        pass

    @abstractmethod
    async def add_customer(self, input_data: dict) -> dict:
        pass
