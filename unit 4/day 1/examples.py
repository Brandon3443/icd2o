import random

def print_1_to_n(n):
    count = 1

    while count <= n:
        print(count)
        count += 1


def get_user_info():
    user_input = ""

    while user_input.lower() not in ['yes', 'no']:
        user_input = input("Do you want to continue? (yes/no): ")
    
    return user_input

def guessing_game(lower, upper):
    target_number = random.randint(lower, upper)
    user_guess = 0

    while user_guess != target_number:
        user_guess = int(input("Guess the number (1-10): "))

    print("Congratulations! You guessed the correct number.")

def validate_password():
    correct_password = "secure123"
    entered_password = ""
    num_attempts = 0
    login_successful = False

    while num_attempts < 3 and entered_password != correct_password:
        entered_password = input("Enter the password: ")
        if num_attempts == 3:
            print("Too many attempts. Login Failed.")
            locked_out = True
        num_attempts+=1

    return locked_out == False
    
def select_option():
    valid_input = False
    while not valid_input:
        print("1. Print Hello")
        print("2. Print World")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Hello")
        elif choice == "2":
            print("World")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")



print_1_to_n(5)
get_user_info()
guessing_game(1,10)

logged_in = validate_password()
if logged_in:
    print('Successful Login')
else:
    print('Unsuccessful Login')

select_option()