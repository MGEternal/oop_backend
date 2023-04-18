from dataclasses import dataclass
from datetime import date

@dataclass
class CodeDiscount():
    code: str
    expire_date: date
    discount: float

    def is_expire(self):
        return self.expire_date > date.today()