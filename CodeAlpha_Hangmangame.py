import random

# List of predefined words
words = ["python", "hangman", "coding", "science", "keyboard"]

# Choose a random word
secret_word = random.choice(words)
guessed_letters = []
attempts_left = 6

print("🎯 Welcome to Hangman!")
print("_ " * len(secret_word))

# Game loop
while attempts_left > 0:
    guess = input("\nGuess a letter: ").lower()

    # Check input validity
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter.")
        continue

    # If already guessed
    if guess in guessed_letters:
        print("🔁 You already guessed that letter!")
        continue

    # Add guess to guessed letters list
    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print("✔️ Good guess!")
    else:
        attempts_left -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts_left}")

    # Display current progress
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    
    print("\n" + display)

    # Check win condition
    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

# If player loses
if attempts_left == 0:
    print("\n💀 Game Over! The word was:", secret_word)
