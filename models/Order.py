from dataclasses import dataclass
from typing import List, Union, Optional
from enum import Enum

from .Payment import Paypal, CreditCard
from .Shipping import Shipping
from .Product import Keyboard, Mouse, Switch, Keycap 

class OrderStatus(Enum):
  OPEN = 0
  CLOSE = 1

@dataclass
class OrderItem:
  product: Union[Keyboard,Mouse,Switch,Keycap]
  qty: int
  price: Optional[float] = 0

@dataclass
class Order:
  items: List[OrderItem]
  status: OrderStatus
  shipping: Shipping
  payment: Union[Paypal,CreditCard]
  email: str

  def is_history_of(self, email):
    if self.email == email:
      return True
  
  # add prcess payment
  def process_payment(self, payment_info):
    if self.payment.pay(payment_info):
      self.status = OrderStatus.CLOSE
      return True
    return False