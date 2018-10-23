# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 20:31:43 2018

@author: user
"""

print ("\n How old are you?"),
age = input()
print("So, you are ",age," years old.")

age = input("how old are you? ")
height = input("How tall are you? ")
weight = input("how much do you weigh? ")
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
#%%
filename = "test.txt"

txt = open(filename)
print(txt.read())
print("type the filename again:")
file_again = input(">")
txt_again = open(file_again)
print(txt_again.read())

#%%
apple = 40
orange =40
banana = 32

if apple < orange:
    print ("Apple is more in the box")  
elif apple > orange:
    print ("orange is more in box")
else:
    print("no. of apple and orange in box")
#%%
test1= [1, "two", 3, "four", 5]
for number in test1:
    if type(number) == int:
        print(number)
    elif type(number) != int:
        print(number)
