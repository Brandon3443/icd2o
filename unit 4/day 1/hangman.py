import random

def word_choice():
    words = ("words", "fortnite", "ishaan", "monkey", "mandem", "bozo", "abrahaaaaaam", "manssss", "AlexLee", "mani", "WaterBottleBeingStolen", "Pulluptothefunction", "typeshit", "L", "skibiditoiletohiorizzler")
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = word_choice()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")

        display = display_word(word_to_guess, guessed_letters)
        print(display)

        if "_" not in display:
            print("Congratulations! You guessed the word.")
            break

    if "_" in display:
        print(f"Sorry, you ran out of attempts. The word was '{word_to_guess}'.")

if __name__ == "__main__":
    hangman()