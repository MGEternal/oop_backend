from pydantic import BaseModel


class SignIn(BaseModel):
    email: str
    password: str

class CartItem(BaseModel):
    product_id: str 
    qty: int

class AddCartItem(BaseModel):
    email: str
    cart_item: CartItem 

class GetCart(BaseModel):
    email: str