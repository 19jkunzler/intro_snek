#!/usr/bin/python3



import os
PWD = os.getcwd()
key = os.listdir(PWD)
size = os.path.getsize
time = os.path.getmtime
creation = os.path.getctime



for file in key:
    tree = dict(file_name=file, file_size=size(file), date_of_creation=creation(file), last_edited=time(file))
    print(tree)











