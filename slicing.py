#!/usr/bin/env python3.7
#script that shows the first last and middle letter of a phrase

message = input("enter a message ")
print("First character", message[0])
print("Last character", message[-1])
print("Middle character", message[int(len(message) / 2 )])
print( "Even characters", message[1::2])
print( "Odd characters", message[::2])
print("Backwords", message[::-1])
