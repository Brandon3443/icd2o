number = int(input("please enter a number: "))
if number > 0:
    print(f"{number} is positive")
if number <= 0:
    print(f"{number} is negative")


age = int(input("please enter your age: "))
if age >= 18:
    print("you are eligible to vote")
if age < 18:
    print("you are not eligible to vote")

str = input("please enter a string: ")
if len(str) == 0:
    print("The string is empty")
if len(str) != 0:
    print("The string is not empty")

def max_number(a, b):
    if a > b:
        return a
    
    return b

print(max_number(4, 5))
print(max_number(14, 5))

def password_checker(password, user_input):
    if password == user_input:
        return True
    return False

pwd = input("password: ")
secret_password = "Ishaan is a mandem"

def range_checker(num, lower, upper):
    if lower <= num <= upper:
        return True
    return False
a = int(input("please enter a number between 1-10: "))
print(range_checker(a, 1, 10)) 
if range_checker(a, 1, 10) == True:
    print("Good you listen to instructions")

if range_checker(a, 1, 10) == False:
    print("Why you gotta be such a monkey")

def grade_converter(grade):
    if grade >= 80:
        print("A")
    if grade >= 70:
        print("B")
    if grade >= 60:
        print("C")
    if grade >= 50:
        print("D")
    if grade < 50:
        print("'F' Your Abe")

