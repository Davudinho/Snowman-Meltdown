# game_logic.py
"""
Core game logic for the Snowman Meltdown game.
Includes gameplay functions and helper utilities.
"""

import random
from ascii_art import STAGES


def get_random_word():
    """Return a random word from a predefined list."""
    words = ["snow", "winter", "cold", "frost", "icicle", "blizzard", "freeze"]
    return random.choice(words)


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Display the snowman ASCII art, mistake count, guessed letters,
    and current word progress.
    """
    print("\n" + "=" * 40)
    print(STAGES[mistakes])
    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    print("-" * 40)

    display_word = " ".join(
        [letter if letter in guessed_letters else "_" for letter in secret_word]
    )

    print(f"Word: {display_word}")
    print("Guessed letters:", ", ".join(guessed_letters) or "None yet")
    print("=" * 40 + "\n")


def handle_guess(guessed_letters):
    """
    Prompt the user for a valid letter input.
    Validates that input is a single alphabetic character and not already guessed.
    """
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️  Please enter exactly ONE alphabetical letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠️  You already guessed that letter!\n")
            continue

        return guess


def play_game():
    """Main game loop for one full play session."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("\n❄️  Welcome to Snowman Meltdown! ❄️")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        if mistakes >= max_mistakes:
            print("💀 The snowman melted! The word was:", secret_word)
            break

        if all(letter in guessed_letters for letter in secret_word):
            print("🎉 Congratulations! You saved the snowman!")
            break

        guess = handle_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print("❌ Wrong guess! The snowman is melting...\n")
        else:
            print("✅ Good guess!\n")


def play_again():
    """Ask the user whether they want to play again."""
    while True:
        again = input("Do you want to play again? (y/n): ").lower().strip()
        if again in ("y", "yes"):
            play_game()
            return
        if again in ("n", "no"):
            print("👋 Thanks for playing Snowman Meltdown! Stay cool!")
            return
        print("⚠️  Please answer with 'y' or 'n'.")
