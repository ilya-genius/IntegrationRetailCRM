from pydantic import BaseModel, field_validator, Field
from datetime import datetime


class OrderItem(BaseModel):
    product_name: str = Field(alias="productName")
    initial_price: float = Field(alias="initialPrice")
    purchase_price: float | None = Field(default=None, alias="purchasePrice")

class CustomerInfo(BaseModel):
    id: int | None = None

class RequestOrder(BaseModel):
    number: str
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    phone: str | None = None
    customer: CustomerInfo | None = None
    items: list[OrderItem]

    @field_validator("email")
    def validate_email(cls, v):
        if v is None:
            return v
        if "@" not in v or "." not in v:
            raise ValueError("Email должен быть корректным e-mail адресом")
        return v


class Contragent(BaseModel):
    contragent_type: str = Field(alias="contragentType")


class Phone(BaseModel):
    number: str


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


class Customer(BaseModel):
    type: str
    id: int
    is_contact: bool = Field(alias="isContact")
    created_at: str = Field(alias="createdAt")
    vip: bool
    bad: bool
    site: str
    contragent: Contragent
    tags: list[str]
    custom_fields: list = Field(alias="customFields")
    personal_discount: float = Field(alias="personalDiscount")
    margin_summ: float = Field(alias="marginSumm")
    total_summ: float = Field(alias="totalSumm")
    average_summ: float = Field(alias="averageSumm")
    orders_count: int = Field(alias="ordersCount")
    segments: list[str]
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    presumable_sex: str | None = Field(None, alias="presumableSex")
    email: str
    customer_subscriptions: list[CustomerSubscription] = Field(alias="customerSubscriptions")
    phones: list[Phone]
    mg_customers: list = Field(alias="mgCustomers")


class DeliveryAddress(BaseModel):
    pass


class Delivery(BaseModel):
    cost: float
    net_cost: float = Field(alias="netCost")
    address: DeliveryAddress


class Order(BaseModel):
    slug: int
    bonuses_credit_total: float = Field(alias="bonusesCreditTotal")
    bonuses_charge_total: float = Field(alias="bonusesChargeTotal")
    id: int
    number: str
    order_type: str = Field(alias="orderType")
    order_method: str = Field(alias="orderMethod")
    privilege_type: str = Field(alias="privilegeType")
    created_at: str = Field(alias="createdAt")
    status_updated_at: str = Field(alias="statusUpdatedAt")
    summ: float
    total_summ: float = Field(alias="totalSumm")
    prepay_sum: float = Field(alias="prepaySum")
    purchase_summ: float = Field(alias="purchaseSumm")
    mark_datetime: str = Field(alias="markDatetime")
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    phone: str
    email: str
    call: bool
    expired: bool
    customer: Customer
    contact: Customer
    contragent: Contragent
    delivery: Delivery
    site: str
    status: str
    items: list
    payments: list
    from_api: bool = Field(alias="fromApi")
    shipped: bool
    links: list
    custom_fields: list = Field(alias="customFields")
    currency: str


class ResponseOrderFull(BaseModel):
    success: bool
    id: int
    order: Order


class RequestAllOrders(BaseModel):
    page: int = Field(default=1, ge=1)
    limit: int = Field(default=20)
    customer_id: int | None = Field(ge=1, default=None)


class ResponseUnit(BaseModel):
    code: str
    name: str
    sym: str

class ResponseOffer(BaseModel):
    displayName: str
    id: int
    xmlId: str
    name: str
    unit: ResponseUnit

class ResponsePrice(BaseModel):
    price: float
    quantity: int

class Item(BaseModel):
    bonusesChargeTotal: float
    bonusesCreditTotal: float
    id: int
    initialPrice: float
    discounts: list = []
    discountTotal: float
    prices: list[ResponsePrice]
    createdAt: datetime
    quantity: int
    status: str
    offer: ResponseOffer
    properties: list = []
    purchasePrice: float
    ordering: int

class ResponseContragent(BaseModel):
    contragentType: str

class ResponsePhone(BaseModel):
    number: str

class ResponseSubscriptionDetails(BaseModel):
    id: int
    channel: str
    name: str
    code: str
    active: bool
    autoSubscribe: bool
    ordering: int

class ResponseCustomerSubscription(BaseModel):
    subscription: ResponseSubscriptionDetails
    subscribed: bool

class ResponseCustomer(BaseModel):
    type: str
    id: int
    isContact: bool
    createdAt: datetime
    managerId: int
    vip: bool
    bad: bool
    site: str
    contragent: ResponseContragent
    tags: list = []
    customFields: list = []
    personalDiscount: float
    marginSumm: float
    totalSumm: float
    averageSumm: float
    ordersCount: int
    costSumm: float | None = 0
    segments: list = []
    firstName: str
    lastName: str
    presumableSex: str | None = None
    email: str
    customerSubscriptions: list[ResponseCustomerSubscription] = []
    phones: list[ResponsePhone]
    mgCustomers: list = []

class ResponseDelivery(BaseModel):
    cost: float
    netCost: float
    address: dict = {}

class ResponsePayment(BaseModel):
    id: int
    type: str
    amount: float
    paidAt: datetime = Field(alias="paidAt")

class ResponseOrder(BaseModel):
    slug: int
    bonusesCreditTotal: float
    bonusesChargeTotal: float
    id: int
    number: str
    orderType: str
    orderMethod: str
    privilegeType: str
    createdAt: datetime
    statusUpdatedAt: datetime
    summ: float
    totalSumm: float
    prepaySum: float
    purchaseSumm: float
    markDatetime: datetime
    lastName: str | None = None
    firstName: str | None = None
    phone: str | None = None
    email: str | None = None
    call: bool
    expired: bool
    managerId: int
    customer: ResponseCustomer
    contact: ResponseCustomer
    contragent: ResponseContragent
    delivery: ResponseDelivery
    site: str
    status: str
    items: list[Item]
    payments: dict[str, ResponsePayment] = {}
    fromApi: bool
    shipped: bool
    customFields: list = []
    currency: str

class ResponsePagination(BaseModel):
    limit: int
    totalCount: int
    currentPage: int
    totalPageCount: int

class ResponseAllOrders(BaseModel):
    success: bool
    pagination: ResponsePagination
    orders: list[ResponseOrder]
