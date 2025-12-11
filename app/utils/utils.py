import json

from app.models.customers import RequestCustomer, RequestAllCustomers
from app.models.orders import RequestOrder, RequestAllOrders
from app.models.payment import RequestPayment


def prepare_retailcrm_payload(model: RequestCustomer) -> dict:
    return {
        "customer": json.dumps(
            model.customer.model_dump(
                by_alias=True,
                exclude_none=True
            )
        )
    }

def prepare_customers_all_payload(model: RequestAllCustomers) -> dict:
    payload = {
        "page": model.page,
        "limit": model.limit,
        "filter[name]": model.name,
        "filter[email]": model.email,
        "filter[dateFrom]": model.date_from.isoformat() if model.date_from else None,
        "filter[dateTo]": model.date_to.isoformat() if model.date_to else None,
    }

    return {k: v for k, v in payload.items() if v is not None}


def prepare_order_payload(order: RequestOrder) -> dict:
    order_dict = {
        "number": order.number,
        "firstName": order.first_name,
        "lastName": order.last_name,
        "email": order.email,
        "phone": order.phone,
        "customer": {"id": order.customer.id} if order.customer and order.customer.id else None,
        "items": [item.model_dump(by_alias=True, exclude_none=True) for item in order.items]
    }

    order_cleaned = {k: v for k, v in order_dict.items() if v is not None}
    return {
        "order": json.dumps(order_cleaned)
    }


def prepare_orders_all_payload(model: RequestAllOrders) -> dict:
    payload = {
        "page": model.page,
        "limit": model.limit,
        "filter[customerId]": model.customer_id
    }

    return {k: v for k, v in payload.items() if v is not None}


def format_datetime_for_api(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def prepare_payment_payload(payment: RequestPayment) -> dict:
    payment_dict = {
        "order": {"id": payment.id},
        "amount": payment.amount,
        "paidAt": format_datetime_for_api(payment.paid_at) if payment.paid_at else None,
        "type": payment.type_payment
    }

    cleaned = {k: v for k, v in payment_dict.items() if v is not None}

    return {
        "payment": json.dumps(cleaned)
    }