# HW1 #
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed = speed - 5

    if speed <= 60:
        return "no ticket"

    if 61 <= speed <= 80:
        return "small ticket"
    return "big ticket"

print(caught_speeding(73, True))
print(caught_speeding(83, True))
print(caught_speeding(83, False))

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
def squirrel_play(temp, summer):
    if summer:
        if 60<= temp <= 100:
            return True
    
        else:
            return False
    elif 60<= temp <=90:
        return True
    else:
        return False
        

# HW 4 #
def in1020(a,b):
    if 10<=a<=20:
        return True
    else:
        return False