# This program says hello and asks for my name.

import time

print('Hello, world!')
print('What is your name?') #ask for their name

myName = input()

print('It is good to meet you, ' + myName)
time.sleep(2)
print('The length of your name is:')
print(len(myName))

print('What is your age?') #ask for their age
myAge = input()
print('You will be ' + str(int(myAge) +1) + ' in a year.')
time.sleep(2)

print('Thank you for playing along!')
time.sleep(2)
print('Goodbye, cruel world.')