# GrayP1
# Date: 8 Sept 2020
# Purpose: Provide user capability to calculate
# volume of a square pyramid

from math import sqrt

# Message to User
print('Let\'s calculate the surface area and volume of a square pyramid...')

# Get inputs from User
# Get base from User
b = float(input("Please enter length of the base in feet: "))

# Get height from User
h = float(input("Please enter height of the pyramid in feet: "))

# Function to calculate the volume using user input
a = (b** 2) * h/3
s = sqrt((h**2) + (b/2)**2)
o = s*b/2

# Display results to user

# Calculations for the volume
print ("The volume is ",a)

# Calculations for the slant height
print ("The slant height is",s)

# Calculations for area of one pyramid side
print ("The area of one pyramid side is: ",o)
