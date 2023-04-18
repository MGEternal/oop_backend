from dataclasses import dataclass, field
from typing import Optional

from .Cart import Cart, CartItem

@dataclass
class User:
    email : str
    firstname : str
    lastname : str
    password : str

    def check_credential(self, email, password):
            return self.email == email and self.password == password
@dataclass
class Admin(User):
        phone : str = field(default="10",metadata={"max_length":10})
        
@dataclass
class Customer(User):
        cart: Optional[Cart] = None

# add item to cart method
        def add_cart_item(self, product, qty): 
                if not self.cart:
                        self.cart = Cart()
                return self.cart.add_item(CartItem(product, qty))