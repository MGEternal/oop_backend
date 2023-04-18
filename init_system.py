from models.System import System
from models.User import Customer
from models.CodeDiscount import *
from models.Category import *
from models.Product import *

system = System()

for i in range(10):
  email = f"email{i+1}@email.com"
  firstname = f"firtname{i+1}"
  lastname = f"lastname{i+1}"
  password = f"passowrd{i+1}"
  system.add_customer(
    Customer(email=email,firstname=firstname,lastname=lastname,password=password)
  )

# mockup for create order

keyboard_cate = Category(name="keybaord")
system.add_category(keyboard_cate)
keyboard_cate.products.append(Keyboard("001","K1 SSR","1200","A mechanical keyboard with RGB backlight","sefaf.png","12","23-03-2023","v4","wireless","blue switches","blacklight"))
keyboard_cate.products.append(Keyboard("002","K2 SSR","1200","A mechanical keyboard with RGB backlight","sefaf.png","12","23-03-2023","v4","wireless","green switches","writelight"))
keyboard_cate.products.append(Keyboard("003","K1 SSR","1400","A mechanical keyboard with RGB backlight","sefaf.png","12","23-03-2023","v4","wireless","brown switches","black"))

customer = system.get_customer_by_email("email1@email.com")


# add code discount
code = CodeDiscount(code="9arm",discount=0.8,expire_date="yy-mm-dd")
system.add_code_discount(code)
  
for i in range(5):
      name = f"cateTest{i+1}"
      
      system.add_category(Category(name=name))

      


# A dictionary to store the discount codes and their discount amount and expiration date 
DISCOUNT_CODES = [
  CodeDiscount(code='CODE1', expire_date=date(2022, 1, 1), discount=0.1),
  CodeDiscount(code='CODE2', expire_date=date(2023, 6, 30), discount=0.2),
  CodeDiscount(code='CODE3', expire_date=date(2024, 2, 2), discount=0.3),
  CodeDiscount(code='CODE3', expire_date=date(2025, 12, 31), discount=0.4),
]

for i in range(len(DISCOUNT_CODES)):
  system.add_code_discount(DISCOUNT_CODES[i])

