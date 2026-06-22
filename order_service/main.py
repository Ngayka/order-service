from fastapi import FastAPI
from order_service.views.orders import router as order_router
from order_service.views.clients import router as client_router
from order_service.views.products import router as product_router


app = FastAPI()


app.include_router(client_router)
app.include_router(product_router)
app.include_router(order_router)


@app.get("/")
def root():
    return{"message": "Orders service is started"}
