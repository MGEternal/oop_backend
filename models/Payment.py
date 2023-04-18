from dataclasses import dataclass
from enum import Enum
from typing import Optional

class PaymentStatus(Enum):
  Unpaid = 0
  Paid = 1
  
@dataclass
class Payment:
  name_on_card: str
  status: PaymentStatus
  transection_id: Optional[str] = None
  date: Optional[str] = None

  def pay(self, payment_info):
    return True
    
class Paypal(Payment):
  pass

class CreditCard(Payment):
  pass