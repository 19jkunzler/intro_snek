#!/usr/bin/env python3.7
#Takes your message and puts it in all capitals and all lowercase, does the title command puts it in a list and shows the first alpabetial word and the last alphabetical word

string = input('Enter a message: ')
print("Uppercase: ", string.upper())
print('lowercase: ', string.lower())
print('Title: ',string.title())
print('Capitalize: ', string.capitalize())
print('List: ', string.split())

words = string.split()

alpha = sorted(words)

print('Alphabetical first word: ', alpha[0])
print('Alphabetical last word: ', alpha[-1])