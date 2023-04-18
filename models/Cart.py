from dataclasses import dataclass, field
from typing import List, Union

from .Product import Keyboard, Switch, Keycap, Mouse

@dataclass
class CartItem:
    product: Union[Keyboard,Keycap,Switch,Mouse] 
    qty: int

    def get_product(self):
        return self.product

    def set_product(self, product):
        self.product = product

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, qty):
        self.qty = qty

@dataclass
class Cart:
    cart_items: List[CartItem] = field(default_factory=list)
    
    def get_cart(self):
        return self.cart_items
    
    def add_item(self, item):
        if isinstance(item, CartItem):
            self.cart_items.append(item)
            return True
        else:
            return False
    
    def remove_item(self, item):
        if item in self.cart_items:
            self.cart_items.remove(item)