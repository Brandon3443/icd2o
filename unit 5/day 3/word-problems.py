def calculate_average_word_length(word_list):
    total_length = 0
 
    for word in word_list:
        total_length += len(word)
    if len(word_list) == 0:
        return 0.0
    average_length = total_length / len(word_list)
    return average_length
 
word_list = ["apple", "kiwi", "banana", "strawberry", "blueberry"]
average_length = calculate_average_word_length(word_list)
print(f"The average length of the words is: {average_length}.")

####################################################################

def is_palindrome(word):
    return word == word[::-1]

def count_palindromic_words(word_list):
    palindromic_count = 0
    palindromic_words = []

    for word in word_list:
        if is_palindrome(word):
            palindromic_count += 1
            palindromic_words.append(word)

    return palindromic_count, palindromic_words

word_list = ["level", "python", "radar", "civic", "list"]

count, palindromic_words = count_palindromic_words(word_list)

print(f"Number of palindromic words: {count}")
print(f"Palindromic words: {palindromic_words}")

####################################################################

def concatenate_strings(string_list):
    result = ' '.join(string_list)
    return result

string_list = ["Hello", "world", "of", "Python", "programming"]

result_string = concatenate_strings(string_list)

print(f"Concatenated string: {result_string}")

####################################################################

def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

def word_vowel_count(word_list):
    result_dict = {}

    for word in word_list:
        result_dict[word] = count_vowels(word)

    return result_dict

word_list = ["apple", "banana", "kiwi", "strawberry", "blueberry"]

result_dictionary = word_vowel_count(word_list)

print("Word Vowel Count Dictionary:")
for word, count in result_dictionary.items():
    print(f"{word}: {count}")

#######################################################################

def alternate_case(word):
    result_word = ""
    for i, char in enumerate(word):
        if i % 2 == 0:
            result_word += char.upper()
        else:
            result_word += char.lower()
    return result_word

def alternate_case_list(word_list):
    result_list = [alternate_case(word) for word in word_list]
    return result_list

word_list = ["python", "programming", "list", "iteration"]

result_alternate_case_list = alternate_case_list(word_list)

print("Words with Alternating Case:")
for word in result_alternate_case_list:
    print(word)

#######################################################################
    
def positive_negatives(lst):
    positives = [num for num in lst if num > 0]
    negatives = [num for num in lst if num < 0]

    return positives, negatives

start_list = [2, 5, -8, 10, -3, 7, 1, -6]

positive_list, negative_list = positive_negatives(start_list)

print("Positive Numbers:", positive_list)
print("Negative Numbers:", negative_list)

#######################################################################

def is_fibonacci(lst):
    for i in range(2, len(lst)):
        if lst[i-1] + lst[i-2] != lst[i]:
            return False
        
    return True

start_list = [0, 1, 1, 2, 3, 5, 8, 13, 21]

print("Is Fibonacci:", is_fibonacci(start_list))

########################################################################

import math
 
def square_roots(lst):
    return [round(math.sqrt(num)) for num in lst]

start_list = [1, 4, 9, 16, 25]

result_list = square_roots(start_list)
print("Square Roots:", result_list)

##########################################################################

def running_average(lst):
    result = []
    total = 0

    for i, num in enumerate(lst, 1):
        total += num
        result.append(total/i)

    return result

##########################################################################

def has_consecutive_pairs(lst):
    for i in range(len(lst)-1):
        if abs(lst[i] - lst[i+1]) == 1:
            return True
        
    return False

start_list = [3, 5, 7, 9, 10, 11, 15]
print("Has Consecutive Pairs:", has_consecutive_pairs(start_list))