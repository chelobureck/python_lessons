from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def test(self):
        pass

class TestCar(Car):
    def car(self):
        return "car"

    def test(self): # type: ignore
        return 'test'


car = TestCar()
print(car.car())
print(car.test())
