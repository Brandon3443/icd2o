# HW 1 #
def cauhgt_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5

    if speed <= 60:
        return "No ticket for you"
    
    if 61 <= speed <= 80:
        return "Small ticket"
    
    return "Big ticket"

print(cauhgt_speeding(73, True))
print(cauhgt_speeding(83, True))
print(cauhgt_speeding(243, True))


# HW 2 #
def add_not_to_string(string: str) -> str:
    if string.startswith("not"):
        return string
    new_string = "not " + string
    return new_string
input_string = input("Enter a string here: ")
output_string = add_not_to_string(input_string)
print(f"The new string is: {output_string}")


# HW 3 #
def in1020(a: int, b: int) -> bool:
    if (a >= 10 and a <= 20) or (b >= 10 and b <= 20):
        return True
    return False 
result1 = in1020(15, 18)
print(f"The result for numbers 15 and 18 is: {result1}")
result2 = in1020(5, 15)
print(f"The result for numbers 5 and 15 is: {result2}")
result3 = in1020(5, 25)
print(f"The result for numbers 5 and 25 is: {result3}")


# HW 4 #
def get_string_character(string: str, front: bool) -> str: 
    if front:
        return string[0]
    return string[-1]
input_string1 = "Hello"
front1 = True
result1 = get_string_character(input_string1, front1)
print(f"The character from the front of the string '{input_string1}' is '{result1}'.")
input_string2 = "World"
front2 = False
result2 = get_string_character(input_string2, front2)
print(f"The character from the back of the string '{input_string2}' is '{result2}'.")