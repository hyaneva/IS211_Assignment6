#!/usr/bin/env python
# coding: utf-8

# In[9]:


import unittest
from conversions_refactored import convert
from conversions_refactored import ConversionNotPossible
from conversions import convertCelsiusToFahrenheit
from conversions import convertCelsiusToKelvin
from conversions import convertFahrenheitToCelsius
from conversions import convertFahrenheitToKelvin
from conversions import convertKelvinToCelsius
from conversions import convertKelvinToFahrenheit


# In[8]:


'''assertAlmostEqual used over assertEqual because 
because floating-point arithmetic can introduce small precision errors. 
Since temperature conversions involve division and multiplication with decimal values, 
the results might have tiny discrepancies and cause errors otherwise'''

class checkTempConversions(unittest.TestCase):

    #Test for Temperature Conversions using the NEW refactored convert function
    def test_temp_conversions(self):
        test_values = [
            ('Celsius', 'Fahrenheit', 0.0, 32.0),
            ('Celsius', 'Kelvin', 0.0, 273.15),
            ('Fahrenheit', 'Celsius', 32.0, 0.0),
            ('Fahrenheit', 'Kelvin', 32.0, 273.15),
            ('Kelvin', 'Celsius', 273.15, 0.0),
            ('Kelvin', 'Fahrenheit', 273.15, 32.0)
        ]
        for from_unit, to_unit, value, expected in test_values:
            result = convert(from_unit, to_unit, value)
            self.assertAlmostEqual(result, expected, places=2)
            print(f"Passed: {value} {from_unit} -> {result} {to_unit} (Expected: {expected} {to_unit})")

            
    #Test for Distance Conversions using the NEW refactored convert function
    def test_distance_conversions(self):
        test_values = [
            ('Miles', 'Yards', 1.0, 1760),
            ('Miles', 'Meters', 1.0, 1609.34),
            ('Yards', 'Miles', 1760, 1.0),
            ('Yards', 'Meters', 1.0, 0.9144),
            ('Meters', 'Miles', 1609.34, 1.0),
            ('Meters', 'Yards', 0.9144, 1.0)
        ]
        for from_unit, to_unit, value, expected in test_values:
            result = convert(from_unit, to_unit, value)
            self.assertAlmostEqual(result, expected, places=2)
            print(f"Passed: {value} {from_unit} -> {result} {to_unit} (Expected: {expected} {to_unit})")

            
    #Test for invalid conversions using the NEW refactored convert function

    def test_incompatible_conversion(self):
        with self.assertRaises(ConversionNotPossible):
            convert("Celsius", "Meters", 100)



    #Test for conversion to the same unit using the NEW refactored convert function
    def test_conversion_to_same_unit(self):
        test_values = [
            ('Celsius', 'Celsius', 100.0),
            ('Fahrenheit', 'Fahrenheit', 212.0),
            ('Kelvin', 'Kelvin', 300.0),
            ('Miles', 'Miles', 5.0),
            ('Yards', 'Yards', 10.0),
            ('Meters', 'Meters', 100.0)
        ]
        for unit, same_unit, value in test_values:
            result = convert(unit, same_unit, value)
            self.assertEqual(result, value)
            print(f"Passed: {value} {unit} -> {result} {same_unit} (Expected: {value} {same_unit})")
    
    
    
    
    
    def test_convertCelsiusToFahrenheit(self):
        #Test conversion from Celsius to Fahrenheit
        test_values = [
            (0.0, 32.0), 
            (100.0, 212.0), 
            (-40.0, -40.0),
            (37.0, 98.6), 
            (300.0, 572.0)
        ]
        for celsius, expected in test_values:
            result = convertCelsiusToFahrenheit(celsius)
            self.assertAlmostEqual(result, expected, places=2)
            print(f"Passed: {celsius}°C -> {result}°F (Expected: {expected}°F)")

            
    def test_convertCelsiusToKelvin(self):
        #Test conversion from Celsius to Kelvin
        test_values = [
            (0.0, 273.15), 
            (100.0, 373.15), 
            (-273.15, 0.0),
            (25.0, 298.15), 
            (300.0, 573.15)
        ]
        for celsius, expected in test_values:
            result = convertCelsiusToKelvin(celsius)
            self.assertAlmostEqual(result, expected, places=2)
            print(f"Passed: {celsius}°C -> {result}K (Expected: {expected}K)")

            
    def test_convertFahrenheitToCelsius(self):
        #Test conversion from Fahrenheit to Celsius
        test_values = [
            (32.0, 0.0), 
            (212.0, 100.0), 
            (-40.0, -40.0),
            (98.6, 37.0), 
            (572.0, 300.0)
        ]
        for fahrenheit, expected in test_values:
            result = convertFahrenheitToCelsius(fahrenheit)
            self.assertAlmostEqual(result, expected, places=2)
            print(f"Passed: {fahrenheit}°F -> {result}°C (Expected: {expected}°C)")

            
    def test_convertFahrenheitToKelvin(self):
        #Test conversion from Fahrenheit to Kelvin
        test_values = [
            (32.0, 273.15), 
            (212.0, 373.15), 
            (-40.0, 233.15),
            (98.6, 310.15), 
            (572.0, 573.15)
        ]
        for fahrenheit, expected in test_values:
            result = convertFahrenheitToKelvin(fahrenheit)
            self.assertAlmostEqual(result, expected, places=2)
            print(f"Passed: {fahrenheit}°F -> {result}K (Expected: {expected}K)")

            
    def test_convertKelvinToCelsius(self):
        #Test conversion from Kelvin to Celsius
        test_values = [
            (273.15, 0.0), 
            (373.15, 100.0), 
            (0.0, -273.15),
            (298.15, 25.0), 
            (573.15, 300.0)
        ]
        for kelvin, expected in test_values:
            result = convertKelvinToCelsius(kelvin)
            self.assertAlmostEqual(result, expected, places=2)
            print(f"Passed: {kelvin}K -> {result}°C (Expected: {expected}°C)")

            
    def test_convertKelvinToFahrenheit(self):
        #Test conversion from Kelvin to Fahrenheit
        test_values = [
            (273.15, 32.0), 
            (373.15, 212.0), 
            (233.15, -40.0),
            (310.15, 98.6), 
            (573.15, 572.0)
        ]
        for kelvin, expected in test_values:
            result = convertKelvinToFahrenheit(kelvin)
            self.assertAlmostEqual(result, expected, places=2)
            print(f"Passed: {kelvin}K -> {result}°F (Expected: {expected}°F)")

if __name__ == "__main__":
    unittest.main()


# In[ ]:




