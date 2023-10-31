import math
def middleThree(string):
    length=len(string)
    mid=length / 2
    result = string[int(mid) - 1:int(mid) + 2]
    return result
print(f"{middleThree('truce')}")
##################################################
def Last_Chars(str_1, str_2):
    first_char_of_a = str_1[0:1]
    last_char_of_b = str_2[len(str_2)-1:len(str_2)]
    return (f"{first_char_of_a}{last_char_of_b}")
print(f"{Last_Chars('mage', 'warrior')}")
##################################################
def last_two(str):
    length = len(str)
    no_last_two = str[0:length-2]
    Last2 = str[length-2:length-1]
    last = str[length-1:length]
    return (f"{no_last_two}{last}{Last2}")
print(last_two("orange"))
##################################################
def extra_front(str):
    result2 = str[0:2] * 3
    return result2
print(extra_front("clockwork"))
###################################################