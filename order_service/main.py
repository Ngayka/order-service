from fastapi import FastAPI
from order_service.views.order import router as order_router

app = FastAPI()

app.include_router(order_router)


@app.get("/")
def root():
    return{"message": "Orders service is started"}
