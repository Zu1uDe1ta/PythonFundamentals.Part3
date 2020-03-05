
print("Give me a number between 1 and 10!")
number = int(input())
from random import randrange
random_number = (randrange(1, 11))

def comparison(random_number, number):
    if random_number > number:
        print("Too low")
    elif random_number < number:
        print("Too high")
    elif random_number == number:
        print("Awesome!")
comparison(random_number, number)

print("The random number was: " + str(random_number))
print("Your guess was: " + str(number))




