def calculate_circle_area(radius):
  print(f"the are of the circle is {radius}")
radius2 = float(input("enter the radius: "))
radius = (3.14*radius2)**2
calculate_circle_area(radius)

def calculate_rectangle_area(length, width):
  print(f"the area of the rectangle is {area}")
length=float(input("enter the legnth"))
width=float(input("enter the width"))
area=length*width
calculate_rectangle_area(length, width)

def calculate_cylinder_volume(radius3, height):
    print(f"the volume of the cylinder is: {volume}")
radius3 = int(input("Please enter radius here: "))
height = int(input("Please enter height here: "))
volume = ((3.14*radius3)**2)*height
calculate_cylinder_volume(radius3, height)

def greet_person(greeting):
  print(f"hello, {greeting}!")
first_name = str(input("what is your first name: "))
last_name = str(input("what is your last name: "))
greeting = first_name + last_name
greet_person(greeting)

def calculate_bmi(weight, height):
  print(f"your BMI is {BMI :.2f}")
weight = float(input("what is your weight in kg: "))
height = float(input("what is your height in meters: "))
BMI = weight/height**2
calculate_bmi(weight, height)

def format_sales(product_name, price, quantity):
  print(f"you purchased {quantity} {product_name}, the total price was ${price :.2f}")
product_name = str(input(" What item did you buy "))
quantity = int(input("how many did you buy "))
price = float(input("what was the total price "))
format_sales(product_name, price, quantity)





