#!/usr/bin/env python3.7
#enter a message to be changed by FizzBuzz
value = int(input("Enter an integer value: "))
#FizzBuzz conditonal statement

if value % 5 == 0 and value % 3 == 0:
    print('FizzBuzz')
elif value % 3 == 0:
    print('Fizz')
elif value % 5 == 0:
    print("Buzz")

else: 
    print(value)
    
    