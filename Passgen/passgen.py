#coding:utf-8                                                                                \
#Function who generate some strong password
import os
from random import randint

def generate_password(number_password, length):
    while number_password != 0:
        number_password = number_password - 1
        password = ""
        for i in range(length):
            password += chr(randint(33, 126))
        passwords.append(password)
    return passwords


passwords = []
