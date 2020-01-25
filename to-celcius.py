#!/usr/bin/env python3.7

# Python implementation here

fahrenheit = input("What temperature (in Fahrenheit) would you like converted to Celsius? ")

celsius = (float(fahrenheit) - 32) * 5 / 9

print(fahrenheit, "F is", celsius, "C")
