from beverage import Beverage


class ColdBeverage(Beverage):
    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price, milliliters)

# a = ColdBeverage('I', 2.4,2.5)


