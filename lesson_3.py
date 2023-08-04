3
from enum import Enum


class Color(Enum):
    RED = '\33[31m'
    GREEN = '\33[32m'
    BLUE = '\33[34m'
    YELLOW = '\33[33m'


class Drawable:
    def draw(self, emoji):
        print(emoji)


class MusicPlayable:
    def play_music(self, song):
        print(f'Now is playing {song}')

    def stop_music(self):
        print(f'Music stopped')


class SmartPhone(MusicPlayable, Drawable):
    pass


class Car(MusicPlayable, Drawable):
    def __init__(self, year, model, color):
        self.__year = year
        self.__model = model
        if isinstance(color, Color):
            self.__color = color
        else:
            raise ValueError('Wrong data type for color')

    @property
    def year(self):
        return self.__year

    @property
    def model(self):
        return self.__model

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        if isinstance(value, Color):
            self.__color = value
        else:
            raise ValueError('Wrong data type for color')

    def __str__(self):
        return f'MODEL: {self.__model} YEAR: {self.__year} ' \
               f'COLOR: {self.__color.value}{self.__color.name}' + '\33[0m'

    def drive(self):
        print(f'Car {self.__model} is driving')

    def __gt__(self, other):
        return self.__year > other.__year

    def __lt__(self, other):
        return self.__year < other.__year

    def __ge__(self, other):
        return self.__year >= other.__year

    def __le__(self, other):
        return self.__year <= other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year


class FuelCar(Car):
    __total_fuel_amount = 1000

    @staticmethod
    def get_fuel_type():
        return 'AI -95'

    @classmethod
    def fill_fuel(cls, amount):
        cls.__total_fuel_amount += amount

    @classmethod
    def get_fuel_amount(cls):
        return cls.__total_fuel_amount

    def __init__(self, year, model, color, fuel_bank):
        Car.__init__(self, year, model, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel_amount -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    @fuel_bank.setter
    def fuel_bank(self, value):
        self.__fuel_bank = value

    def __str__(self):
        return super().__str__() + f' FUEL BANK: {self.__fuel_bank}'

    def drive(self):
        print(f'Car {self.model} is driving using fuel')

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class ElecricCar(Car):
    def __init__(self, year, model, color, battery):
        Car.__init__(self, year, model, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def __str__(self):
        return super().__str__() + f' BATTERY: {self.__battery}'

    def drive(self):
        print(f'Car {self.model} is driving by electricity')


class HybridCar(FuelCar, ElecricCar):
    def __init__(self, year, model, color, fuel_bank, battery):
        FuelCar.__init__(self, year, model, color, fuel_bank)
        ElecricCar.__init__(self, year, model, color, battery)


print(f'Fuel cars factory has: {FuelCar.get_fuel_amount()} '
      f'{FuelCar.get_fuel_type()} litters.')
some_car = Car(2022, 'Nissan X-Trail', Color.RED)
print(some_car)

fuel_car = FuelCar(2000, 'Toyota Camry', Color.BLUE, 65)
print(fuel_car)

electric_car = ElecricCar(2023, 'Tesla Model X', Color.GREEN, 25000)
print(electric_car)

hybrid_car = HybridCar(2021, 'Toyota Prius', Color.YELLOW, 45, 10000)
print(hybrid_car)
hybrid_car.drive()

print(HybridCar.mro())

number_1 = 15
number_2 = 7
print(f'Number one is bigger than Number two: {number_1 > number_2}')
print(f'Camry is better than Model X: {fuel_car > electric_car}')
print(f'Camry car is not the same with Model X: {fuel_car != electric_car}')

print(f'Sum of numbers: ' + str(number_1 + number_2))
print(f'Total fuel banks: ' + str(fuel_car + hybrid_car))

print(f'Fuel cars factory has: {FuelCar.get_fuel_amount()} '
      f'{FuelCar.get_fuel_type()} litters.')
# FuelCar.__total_fuel_amount -= 100
# print(f'Fuel cars factory has: {FuelCar.total_fuel_amount} litters.')
FuelCar.fill_fuel(500)
print(f'Fuel cars factory has: {FuelCar.get_fuel_amount()} '
      f'{FuelCar.get_fuel_type()} litters.')
hybrid_car.play_music('Song 1')
hybrid_car.stop_music()
hybrid_car.draw('🏎️')

samsung = SmartPhone()
samsung.play_music('Favorite song')
samsung.draw('📱')

if electric_car.model == 'Tesla Model X':
    print('This car is cool!')

if electric_car.color == Color.GREEN:
    print('This car is beautiful!')