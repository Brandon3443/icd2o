import math

# arguments:
# function name:
# what does it return: 
def calculate_cylinder_volume(radius, height):
    return math.pi * radius**2 * height

def calculate_circle_area(radius):
    return math.pi * radius**2

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def convert_temperature(degrees, scale):
    if scale.lower() == 'celsius':
        fahrenheit = (degrees * 9/5) + 32
        return fahrenheit
    elif scale.lower() == 'fahrenheit':
        celsius = (degrees - 32) * 5/9
        return celsius
    else:
        return None

def larger_string(string_a, string_b):
    len_a = len(string_a)
    len_b = len(string_b)

    if len_a > len_b:
        return string_a
    elif len_b > len_a:
        return string_b
    else:
        return "Same"
    
def first_two(str):
    return str[0:2]