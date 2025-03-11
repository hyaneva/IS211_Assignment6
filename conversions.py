#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = 0
    
    return fahrenheit


def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = 0
    
    return kelvins


def convertFahrenheitToCelsius(fahrenheit):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    celsius = 0
    
    return celsius


def convertFahrenheitToKelvin(fahrenheit):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = 0
    
    return kelvins


def convertKelvinToCelsius(kelvins):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    celsius = 0
    
    return celsius


def convertKelvinToFahrenheit(kelvins):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    fahrenheit = 0
    
    return fahrenheit'''


# In[2]:


def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = celsius + 273.15
    return kelvins


def convertFahrenheitToCelsius(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def convertFahrenheitToKelvin(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Kelvins"""
    kelvins = (fahrenheit - 32) * 5/9 + 273.15
    return kelvins


def convertKelvinToCelsius(kelvins):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Celsius"""
    celsius = kelvins - 273.15
    return celsius


def convertKelvinToFahrenheit(kelvins):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = (kelvins - 273.15) * 9/5 + 32
    return fahrenheit


# In[ ]:




