class Transport:
    def __init__(self, theModel, theYear, theColor,):
        self.model = theModel
        self.year = theYear
        self.color = theColor
    
    def changeColor(self, newColor):
        self.color = newColor

class Plane(Transport):
    def __init__(self, theModel, theYear, theColor):
        super().__init__(theModel, theYear, theColor)   


class Car(Transport):
    counter = 0
    number_wheels = 10
    
    # constructor
    def __init__(self, theModel, theYear, theColor, penaltes=0):
        # atributes/fields
        super().__init__(theModel, theColor, theYear,)
        self.penaltes = penaltes
        Car.counter += 1
        
    # method
    def drive(self, city):
        print(f'Car: {self.model} is driving to {city}')
        
    # method 
    def changeColor(self, newColor):
        self.color = newColor
        
class Truck(Car):
    def __init__(self, theModel, theYear, theColor, penaltes=0, loadCapacity=1000):
        super().__init__(theModel, theYear, theColor, penaltes)
        self.loadCapacity = loadCapacity
        
    def loadCargo(self, weigth, type):
        if weigth > self.loadCapacity:
            print(f'you can not load more than {self.loadCapacity}!')
        else:
            print(f'You successfully loaded cargo of {type} ({weigth}kg)'
                  f'on {self.model}')
        
        
toyotoTrack = Truck('Toyota Hilux', 2023, 'Red', 500, 1000)
print(f'Model: {toyotoTrack.model}, Year: {toyotoTrack.year},\n'
      f'Color: {toyotoTrack.color}, Penalties: {toyotoTrack.penaltes}\n'
      f'load capacity: {toyotoTrack.loadCapacity}kg')
# toyotoTrack.loadCargo(2000, 'apples')
toyotoTrack.loadCargo(900, 'potatoes')
        

price_of_trucks_winter_lastic = 10000
our_cars = 3

print(f'We need {our_cars * Car.number_wheels * price_of_trucks_winter_lastic} soms to buy winter lastics of trucks')
        
# boeingPlane = Plane('Boeing 737', 2022, 'White')
# print(f'Model: {boeingPlane.model}, Year: {boeingPlane.year}, Color: {boeingPlane.color}')
        

# bmw_car = Car('BMW M5', '2015', 'Black')
# print(bmw_car)
# print(f'Model: {bmw_car.model}, Year: {bmw_car.year}, Color: {bmw_car.color}')
# hondaCar = Car(theYear=2020, penaltes=1200, theModel='honda CR-V', theColor='Silver')
# print(f'Model: {hondaCar.model}, Year: {hondaCar.year}, Color: {hondaCar.color}, Penalties: {hondaCar.penaltes}')

# hondaCar.color = 'Green'
# hondaCar.changeColor(newColor='Purpul')
# print(f'New color: {hondaCar.color}')


# bmw_car.drive('Osh')
# bmw_car.drive('Tokmok')
# print(f'Number of cars: {Car.counter}')
# print(f'We need {our_cars * Car.number_wheels * price_of_winter_lastic} soms to buy winter lastics')