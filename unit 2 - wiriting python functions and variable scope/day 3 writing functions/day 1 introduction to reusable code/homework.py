# Function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        return length * width
    else:
        return "Invalid input. Please provide numeric values for length and width."

# Function to check if a string contains a specific substring
def contains_substring(string, substring):
    if isinstance(string, str) and isinstance(substring, str):
        return substring in string
    else:
        return "Invalid input. Please provide two strings."

# Function to calculate the average of three floats
def average_of_three_floats(num1, num2, num3):
    if all(isinstance(x, float) for x in [num1, num2, num3]):
        return (num1 + num2 + num3) / 3.0
    else:
        return "Invalid input. Please provide three floating-point numbers."

# Function to concatenate two strings
def concatenate_strings(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        return str1 + str2

# Function to calculate the volume of a cube
def volume_of_cube(side_length):
    if isinstance(side_length, (int, float)):
        return side_length ** 3

# Function to check if a number is positive, negative, or zero
def check_number_status(number):
    if isinstance(number, (int, float)):
        if number > 0:
            return "Positive"
        elif number < 0:
            return "Negative"
        else:
            return "Zero"

# Function to calculate the circumference of a circle
def circumference_of_circle(radius):
    if isinstance(radius, (int, float)):
        return 2 * 3.141592653589793 * radius

# Function to count the number of occurrences of a character in a string
def count_char_occurrences(string, char):
    if isinstance(string, str) and isinstance(char, str) and len(char) == 1:
        return string.count(char)

# Function to calculate the percentage of a number
def calculate_percentage(number, percentage):
    if isinstance(number, (int, float)) and isinstance(percentage, (int, float)):
        return (percentage / 100) * number

# Function to find the absolute difference between two numbers
def absolute_difference(num1, num2):
    if all(isinstance(x, (int, float)) for x in [num1, num2]):
        return abs(num1 - num2)

# Function to capitalize the first letter of a string
def capitalize_first_letter(string):
    if isinstance(string, str):
        return string.capitalize()

# Function to calculate the square of a number
def square(number):
    if isinstance(number, (int, float)):
        return number ** 2

# Function to find the maximum of two numbers
def max_of_two(num1, num2):
    if all(isinstance(x, (int, float)) for x in [num1, num2]):
        if num1 > num2:
            return num1
        else:
            return num2

# Function to calculate the square root of a number
def square_root(number):
    if isinstance(number, (int, float)) and number >= 0:
        return number ** 0.5

# Function to find the length of a string
def length(input_data):
    if isinstance(input_data, str):
        return len(input_data)

#######################################################################################################

#HW1 
length = int(input("please enter the length: "))
width = int (input("please enter the width: "))

area = area_of_rectangle(length, width)

print(f"the area is {area} square units")
#HW2
def contains_substring(string, substring):
    if isinstance(string, str) and isinstance(substring, str):
        return substring in string
    else:
        return "Invalid input. Please provide two strings."

#HW3
float1 = float(input("please enter a float: "))
float2 = float(input("please enter a float: "))   
float3 = float(input("please enter a float: "))
average= average_of_three_floats(float1,float2,float3)

print(f"{average}")

#HW4
str1 = int(input("enter a string: "))
str2 = int(input("enter a string: "))

con = concatenate_strings
print(f"{con}")

#HW5
side = str(input("enter the side length for a cube: "))
vol = volume_of_cube(side)
print(vol)

#HW6
num = int(input("please slide a number: "))
check = check_number_status(num)
print(f" the number is {check}")

#HW7
R = int(input("please eneter the radius: "))
circum = circumference_of_circle(R)
print(circum)

