

def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

if __name__ == "__main__":
    calculate(3, add=3, multiply=5)

    #my_car = Car(make="Nissan")
    #print(my_car.model)


class Car:

    def __init__(self, **kw):
        super(Car, self).__init__()
        self.make = kw["make"]
        self.model = kw["model"]
        self.colour = kw.get("colour")


