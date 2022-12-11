#Password Generator V2
import random

print("Welcome to Password Generator")
chars = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz"
spec_chars = "!@?#()*&^%$E"
numbers = "123456789"

length=int(input("Length of Password: "))
special_chars=int(input("No of Special Characters: "))
number_chars=int(input('No of numbers: '))


if number_chars>length:
    print('The amount of numbers cannot be greater than total number of characters.')
elif special_chars>length:
    print('The amount of special characters cannot be greater than total number of characters.')
elif number_chars+special_chars>length:
    print('You cannot have that many numbers and special characters as it is greater than the password length.')
else:
    random_characters=random.choices(chars, k=length-special_chars-number_chars)
    random_specchars=random.choices(spec_chars, k=special_chars)
    random_numbers=random.choices(numbers, k=number_chars)
    password="".join(random.sample(random_characters+random_numbers+random_specchars, k=length))
    print(password)