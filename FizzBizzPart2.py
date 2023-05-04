#!/usr/bin/env python3.7
#enter a message to be changed by FizzBuzz
value = int(input("How many values should we process: "))
#FizzBuzz conditonal statement

for number in range(1, value + 1):
    if number % 5 == 0 and number % 3 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print("Buzz")

    else: 
        print(number)