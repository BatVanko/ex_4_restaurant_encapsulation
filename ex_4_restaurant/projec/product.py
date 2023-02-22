class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

# p1 = Product('Ivan', 24.5)
# p1.name = 'i'
# print(p1.name)
