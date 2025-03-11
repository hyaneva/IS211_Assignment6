#!/usr/bin/env python
# coding: utf-8

# In[7]:


class ConversionNotPossible(Exception):
    pass

# Conversion functions for temperature and distance
def convert(fromUnit, toUnit, value):
    print(f"Converting from {fromUnit} to {toUnit} with value {value}")
    
    # Check if the units are in the same category (temperature or distance)
    temperature_units = ['Celsius', 'Fahrenheit', 'Kelvin']
    distance_units = ['Miles', 'Yards', 'Meters']
    
    # If fromUnit and toUnit are in different categories, raise an exception
    if (fromUnit in temperature_units and toUnit in distance_units) or (fromUnit in distance_units and toUnit in temperature_units):
        raise ConversionNotPossible(f"Cannot convert from {fromUnit} to {toUnit} as they belong to different categories.")
    
    # Check if units are the same
    if fromUnit == toUnit:
        print(f"Units are the same: {fromUnit}. Returning original value.")
        return value

    # Temperature conversion logic
    if fromUnit in temperature_units and toUnit in temperature_units:
        if fromUnit == 'Celsius':
            if toUnit == 'Fahrenheit':
                return (value * 9/5) + 32
            elif toUnit == 'Kelvin':
                return value + 273.15
        elif fromUnit == 'Fahrenheit':
            if toUnit == 'Celsius':
                return (value - 32) * 5/9
            elif toUnit == 'Kelvin':
                return (value - 32) * 5/9 + 273.15
        elif fromUnit == 'Kelvin':
            if toUnit == 'Celsius':
                return value - 273.15
            elif toUnit == 'Fahrenheit':
                return (value - 273.15) * 9/5 + 32
    
    # Distance conversion logic
    if fromUnit in distance_units and toUnit in distance_units:
        if fromUnit == 'Miles':
            if toUnit == 'Yards':
                return value * 1760
            elif toUnit == 'Meters':
                return value * 1609.34
        elif fromUnit == 'Yards':
            if toUnit == 'Miles':
                return value / 1760
            elif toUnit == 'Meters':
                return value * 0.9144
        elif fromUnit == 'Meters':
            if toUnit == 'Miles':
                return value / 1609.34
            elif toUnit == 'Yards':
                return value / 0.9144
    
    # If neither, raise an exception
    raise ConversionNotPossible(f"Cannot convert from {fromUnit} to {toUnit}")

