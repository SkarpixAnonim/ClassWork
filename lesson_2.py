class Contact:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city
    
    @property
    def street(self):
        return self.__street
    
    @property
    def number(self):
        return self.__number


class Animal:
    def __init__(self, name, age, contact):
        self.__name = name
        
        if isinstance(contact, Contact):
            self.__contact = contact
        else:
            raise ValueError('Wrong value for age attributes. It mustbe positiv number.')
        if isinstance(age, int) and age > 0:
            self.__age = age
        else:
            raise ValueError('Wrong value for age attributes. It mustbe positiv number.')
        
        self.__was_born()
            
    def __was_born(self):
        print(f"Animal {self.__name} was born")
    
    def getName(self):
        return self.__name
        
    def getAge(self):
        return self.__age
    
    def setAge(self, newAge):
        if isinstance(newAge, int) and newAge > 0:
            self.__age = newAge
        else:
            raise ValueError('Wrong value for age attributes. It mustbe positiv number.')
        
    def info(self):
        return f'Name: {self.__name}, Age: {self.__age}, Birth age: {2023 - self.__age}\n' \
               f'Contact info: {self.__contact.city}, {self.__contact.street}, {self.__contact.number}'
    
    def speak(self):
        return self.__speak
    
    def speak(self):
        raise NotImplementedError('j')
        
        
class Fish(Animal):
    def __init__(self, name, age, contact):
        super(Fish, self).__init__(name, age, contact)
        
    def speak(self):
        pass
        
        
class Dog(Animal):        
    def __init__(self, name, age, commands, contact, speak):
        super(Dog, self).__init__(name, age, contact)
        self.__commands = commands
        self.__speak = speak
        
    @property
    def commands(self):
        return self.__commands
    
    @commands.setter
    def commands(self, value):
        self.__commands = value
    
    def info(self):
        return super().info() + f', Commands: {self.__commands}'
    
    def speak(self):
        return self.__speak
    
class Cat(Animal):
    def __init__(self, name, age, contact, speak):
        super(Cat, self).__init__(name, age, contact)
        self.__speak = speak
    
    def speak(self):
        return self.__speak


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins, contact, speak):
        super(FightingDog, self).__init__(name, age, commands, contact, speak)
        self.__wins = wins
        self.__speak = speak
    
    @property
    def wins(self):
        return self.__wins
    
    @wins.setter
    def wins(self, value):
        self.__wins = value
        
    def info(self):
        return super().info() + f', Wins: {self.__wins}'
    
    def speak(self):
        return self.__speak
        
        
        
contact_1 = Contact('Bishkek', 'Salieva', 55)
fightingDog = FightingDog('Rex', 1, 'Fight', 7, contact_1, 'GAV-GAV!!!')
cat = Cat('Tom', 3, contact_1, 'Miyu')
dog = Dog('Sasiska', 6, 'Sit', contact_1, 'GAV!')
dog.commands = 'Sit, bark'
print(dog.commands)

fish = Fish('Dori', 2, contact_1)
        
        
# someAnimal = Animal('Kalys', 2)
# # someAnimal.age = 'Five years old'
# someAnimal.setAge(7)
# print(someAnimal.info())
# print(someAnimal.getAge())
# someAnimal.wa
    
animal_list = [fish, dog, cat, fightingDog]

for animal in animal_list:
    print(animal.info())
    print(animal.speak())