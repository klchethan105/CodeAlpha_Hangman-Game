import random

# Predefined list of words
words = ["python", "flask", "github", "hangman", "program"]

# Select a random word from the list
word_to_guess = random.choice(words)
guessed_letters = []
attempts_left = 6

print(" Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# Game loop
while attempts_left > 0:
    # Display the current progress
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print("\nWord:", display_word)

    # Check if the player has guessed all letters
    if "_" not in display_word:
        print(" Congratulations! You guessed the word:", word_to_guess)
        break

    # Player input
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word_to_guess:
        print(" Good guess!")
    else:
        attempts_left -= 1
        print(f" Wrong guess! Attempts left: {attempts_left}")

# If the player runs out of attempts
if attempts_left == 0:
    print(" Game over! The word was:", word_to_guess)
