from random import randint, choices
import calculator
import emoji
from decouple import config
from termcolor import cprint
from person import Person
#code start
print(randint(2, 10))
print(calculator.multiplication(4, 7))


myFriend = Person('Jim', 20)
cprint('Hello world', 'green', 'on_red')
print(emoji.emojize('Python is :thumbs_up:'))
print(config('DATABASE_URL'))
commented = config('COMMENTED', default=0)
print(commented)
