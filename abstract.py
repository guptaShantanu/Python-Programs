from abc import ABCMeta,abstractmethod
class Product(metaclass=ABCMeta):
    @abstractmethod
    def return_policy(self):
        pass

class Furniture(Product):

    def return_policy(self):
        print("ghj hg ")

class Mobile(Product):
    def return_policy(self):
        print("All mobiles must be returned within 10 days of purchase")

class Shoe(Product):
    def return_policy(self):
        print("All shoes must be returned within 7 days of purchase")

f=Furniture()
