def calculate_circle_area(radius):
   print(f"the area of the circle is: {radius}")
radius2 = int(input("Please enter radius here: "))
radius = (3.14*radius2)**2
calculate_circle_area(radius)
##################################
def calculate_rectange_area(length, width):
    print(f"the area of the rectangle is: {area}")
length = int(input("Please enter length here: "))
width = int(input("Please enter width here: "))
area = length * width
calculate_rectange_area(length, width)
##################################
def calculate_cylinder_volume(radius3, height):
    print(f"the volume of the cylinder is: {volume}")
radius3 = int(input("Please enter radius here: "))
height = int(input("Please enter height here: "))
volume = ((3.14*radius3)**2)*height
calculate_cylinder_volume(radius3, height)
##################################
def greet_person(greeting):
    print(f"Hello, {first_name} {last_name}!")
first_name = str(input("Please enter your first name here: "))
last_name = str(input("Please enter your last name here: "))
greeting = first_name + last_name
greet_person(greeting)
##################################
def format_sales(price):
    print(f"You purchased {quantity} {product} for a total of ${price}.")
quantity = int(input("Please enter the quantity amount here: "))
product = str(input("Please enter the product name here: "))
price2 = float(input("Please enter the price rounded to 2 decimals here: "))
price = price2 * quantity
format_sales(price)
##################################
def calculate_bmi(weight):
    print(f"Your weight is: {weight}lbs.")
weight = float(input("Please enter your weight with 2 decimal places here: "))
calculate_bmi(weight)
##################################