# Properties1

# hadaf: nemikhahim object ba meghdar < 0 ijad shavad
class Product:
    def __init__(self, price):
        self.price = price


product = Product(-10)
# dar in method control vojood nadarad.

# ----------------
# hadaf : making this property "private"


class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product = Product(10)
# in raah "gheyre pythonic" ast. raah badi in ast ke property ijad konim


class Product3:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError(f"You Entered {value}.\nPrice cannot be negative")
        self.__price = value
    # property yek function default Python ast
    price = property(get_price, set_price)

# ----------------------------


class Product4:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError(f"You Entered {value}.\nPrice cannot be negative")
        self.__price = value
    # property yek function default Python ast


product4 = Product4(-20)

print(product4.price)
