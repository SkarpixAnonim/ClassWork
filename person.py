class Person:
    def __init__(self, fullname, age):
        self.__fullname = fullname
        self.__age = age
        
    def __str__(self):
        return f'Full name: {self.__fullname}\n'\
            f'Age: {self.__age}'
            

if __name__ == '__main__':           
    person = Person('Jhon', 32)
    print(person)