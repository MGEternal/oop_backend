from fastapi import APIRouter, HTTPException
from init_system import system
from schemas.customer_shcema import SignIn, AddCartItem, GetCart 

router = APIRouter(prefix="/customer")

@router.get("/get_all")
async def get_all_customer():
    return { "data": system.customers }

@router.post("/sign_in")
async def customer_login(body: SignIn):
    customer = system.sign_in(body.email, body.password)
    if not customer:
        raise HTTPException(status_code=400, detail="Wrong email or password")
    return { "message": "Sign in successful", "data": customer }

@router.post("/add_cart")
async def add_cart_item(body: AddCartItem):
    email = body.email
    item_id = body.cart_item.product_id
    qty = body.cart_item.qty
    
    customer = system.find_customer_by_email(email)
    product = system.find_product_by_id(item_id)

    if customer and product:
        customer.add_cart_item(product, qty)
        return { "message": "success" }
    else:
        raise HTTPException(status_code=400, detail="Something went wrong")

@router.get("/viewcart")
async def view_cart(body: GetCart):
    customer = system.get_customer_by_email(body.email)
    return customer.cart