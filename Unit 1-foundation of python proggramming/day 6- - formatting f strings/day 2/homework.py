def say_hello(name):
    print(f"Hello there {name}")

name = str(input("Please enter your name here: "))

say_hello(name)
#########################################################
def multiply(answer):
    print(f"Your product is {answer}")

num1 = int(input("Enter number 1 here: "))
num2 = int(input("Enter number 2 here: "))

answer = num1 * num2

multiply(answer)
#########################################################
def calculate_power(answer2):
    print(f"The answer is: {answer2}")

number1 = int(input("Please enter a number: "))
exponent = int(input("Please enter an exponent: "))

answer2 = number1**exponent

calculate_power(answer2)
#########################################################
def calculate_circle_area(area):
    print(f"The area of the circle is: {area} units")

radius = int(input("Enter radius here: "))

area = 3.14*(radius*radius)
calculate_circle_area(area)
#########################################################
def calculate_triangle_area(area2):
    print(f"The area of the triangle is: {area2}")

base = int(input("Enter base here: "))
height = int(input("Enter height here: "))

area2 = (base * height) / 2

calculate_triangle_area(area2)
#########################################################
def calculate_cylinder_volume(volume):
    print(f"THe volume of the cylinder is: {volume}")

radius2 = int(input("Enter radius for cylinder here: "))
height2 = int(input("Enter height for cylinder here: "))

volume = ((3.14 * radius2) ** 2) * height2

calculate_cylinder_volume(volume)
#########################################################
def print_triangle(char2):
    print(f"{char2:>10}")
    print(f"{char2:>9} {char2:>1}")
    print(f"{char2:>8} {char2:>3}")
    print(f"{char2:>7} {char2:>5}")
    print(f"{char2:>6} {char2:>7}")
    print(f"{char2:>5} {char2:>9}")
    print(f"{char2:>4} {char2:>11}")
    print(f"{char2:>3} {char2:>13}")
    print(f"{char2:>2} {char2:>15}")
    print(f"{char2:>2} {char2:>2} {char2:>2} {char2:>2} {char2:>2} {char2:>2}")
    
char2 = input(print("Enter character here: "))

print_triangle(char2)
#########################################################
def print_square(char3):
    print(f"{char3} {char3:>2} {char3:>2} {char3:>2} {char3:>2} {char3:>2}")
    print(f"{char3} {char3:>15}")
    print(f"{char3} {char3:>15}")
    print(f"{char3} {char3:>15}")
    print(f"{char3} {char3:>15}")
    print(f"{char3} {char3:>15}")
    print(f"{char3} {char3:>15}")
    print(f"{char3} {char3:>2} {char3:>2} {char3:>2} {char3:>2} {char3:>2}")

char3 = input(print("Enter character here: "))

print_square(char3)
