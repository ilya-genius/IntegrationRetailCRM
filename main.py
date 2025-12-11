import uvicorn
from fastapi import FastAPI, Request
from app.routers.customers import customer_router
from app.routers.orders import order_router
from app.routers.payment import payment_router
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=422,
        content={"message": str(exc)},
    )

app.include_router(customer_router)
app.include_router(order_router)
app.include_router(payment_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8880,
        reload=False
    )