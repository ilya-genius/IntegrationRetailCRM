from pydantic import BaseModel, Field, field_validator
from datetime import date


class Phone(BaseModel):
    number: str = Field(alias="number")


class Customer(BaseModel):
    first_name: str | None = Field(alias="firstName")
    last_name: str | None = Field(alias="lastName")
    email: str | None = Field(alias="email")
    phones: list[Phone] | None = Field(default=None, alias="phones")

    @field_validator("email")
    def validate_email(cls, v):
        if v is None:
            return v
        if "@" not in v or "." not in v:
            raise ValueError("Email должен быть корректным e-mail адресом")
        return v


class RequestCustomer(BaseModel):
    customer: Customer


class ResponseCustomer(BaseModel):
    success: bool
    id: int


class SubscriptionInfo(BaseModel):
    id: int
    channel: str
    name: str
    code: str
    active: bool
    auto_subscribe: bool = Field(alias="autoSubscribe")
    ordering: int


class CustomerSubscription(BaseModel):
    subscription: SubscriptionInfo
    subscribed: bool


class Contragent(BaseModel):
    contragent_type: str = Field(alias="contragentType")


class Pagination(BaseModel):
    limit: int
    total_count: int = Field(alias="totalCount")
    current_page: int = Field(alias="currentPage")
    total_page_count: int = Field(alias="totalPageCount")


class RetailCustomer(BaseModel):
    type: str
    id: int
    is_contact: bool = Field(alias="isContact")
    created_at: str = Field(alias="createdAt")
    vip: bool
    bad: bool
    site: str
    contragent: Contragent
    tags: list[str]
    custom_fields: list = Field(default_factory=list, alias="customFields")
    personal_discount: float = Field(alias="personalDiscount")
    margin_summ: float = Field(alias="marginSumm")
    total_summ: float = Field(alias="totalSumm")
    average_summ: float = Field(alias="averageSumm")
    orders_count: int = Field(alias="ordersCount")
    segments: list
    first_name: str | None = Field(default=None, alias="firstName")
    last_name: str | None = Field(default=None, alias="lastName")
    presumable_sex: str | None = Field(default=None, alias="presumableSex")
    email: str | None = None
    customer_subscriptions: list[CustomerSubscription] = Field(alias="customerSubscriptions")
    phones: list[Phone]
    mg_customers: list = Field(alias="mgCustomers")


class ResponseAllCustomers(BaseModel):
    success: bool
    pagination: Pagination
    customers: list[RetailCustomer]


class RequestAllCustomers(BaseModel):
    page: int = Field(default=1, ge=1)
    limit: int = Field(default=20)
    name: str | None = None
    email: str | None = None
    date_from: date | None = None
    date_to: date | None = None

    @field_validator("limit")
    def check_limit(cls, v):
        if v not in (20, 50, 100):
            raise ValueError("limit должен быть 20, 50 или 100")
        return v

    @field_validator("email")
    def validate_email(cls, v):
        if v is None:
            return v
        if "@" not in v or "." not in v:
            raise ValueError("Email должен быть корректным e-mail адресом")
        return v
