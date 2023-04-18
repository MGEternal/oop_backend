from enum import Enum
from dataclasses import dataclass
from typing import Optional

class ShippingMethod(Enum):
  STANDART = 0
  EMS = 1

@dataclass
class ConfirmShipping:
  tracking_no: str
  date: str
  method: ShippingMethod 
 
@dataclass
class Shipping:
  firstname: str
  lastname: str
  address: str
  phone: str
  zip_code: str
  confirm_shipping: Optional[ConfirmShipping] = None