from fastapi import FastAPI,APIRouter
router = APIRouter()
app = FastAPI()

from controllers import customer_ctrl
from controllers import order_ctrl
from controllers import product_ctrl

app.include_router(customer_ctrl.router)
app.include_router(order_ctrl.router)
app.include_router(product_ctrl.router)
