# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:53:41 2019

@author: Lenovo
"""

import random
restaurantlist=['a','b','c','d','e']
def pickrestaurant():
    print(restaurantlist[random.randint(0,len(restaurantlist)-1)])
def addrestaurant(name):
    restaurantlist.append(name)
def removerestaurant(name):
    restaurantlist.remove(name)
def listrestaurant():
    for restaurant in restaurantlist:
        print(restaurant)
while True:
    print(''' [1]-List Restaurant
          [2]- Add Restaurant
          [3]- remove restaurant
          [4]-Pick restaurant
          .....''')
    selection=input('Please select one option:')
    if selection=='1':
        listrestaurant()
    elif selection=='2':
        inName=input('Type name of the restaurant:')
        addrestaurant(inName)
    elif selection=='3':
        inName=input('Type the bname of the restaurant that you want to remove:')
        removerestaurant(inName)
    elif selection=='4':
        pickrestaurant()
    elif selection=='5':
        break
    else:
        print('Slected wrong option')
    