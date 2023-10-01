#!/usr/bin/env python
# coding: utf-8

# In[1]:


# celsius to farhenheit
def Celsius_to_Farhenheit(Celsius):
    return (Celsius * 9/5) + 32
# fahrenheit to celsius
def Farhenheit_to_Celsius(Farhenheit):
    return (Farhenheit - 32) * 5/9


# In[2]:


conversion_features = {
        'c': Celsius_to_Farhenheit,
        'f': Farhenheit_to_Celsius}
print("Choose the conversion direction.")
print("Put C for celsius to farhenheit or F for farhenheit to celsius")

choice = input("Enter your choice: ").strip().lower()

if choice in conversion_features:
    temperature = float(input("Enter the temperature: "))
    
    # Conversion 
    converted_temperature = conversion_features[choice](temperature)
    
    print(f"{temperature} degrees {'Celsius' if choice == 'c' else 'Farhenheit'} is {converted_temperature} degrees {'Farhenheit' if choice == 'c' else 'Celsius'}")  
else:        
    print("this was not a valid input. Please enter a C of a F.")

