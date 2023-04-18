from typing import List
from .Product import Product

class Category:
    def __init__(self,name):
        self.__name = name
        self.products = []
        
    @property
    def name(self):
        return self.__name
    
    def add_products(self, products):
        self.__products.append(products)
        
    def get_product_by_id(self, id):
        for product in self.products:
            if id == product.id:  
                return product
        return False

    def get_product_by_name(self, name):
        for product in self.products:
            if name == product.name:
                return product
        return False