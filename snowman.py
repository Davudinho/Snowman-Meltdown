# snowman.py

from game_logic import play_game, play_again

if __name__ == "__main__":
    play_game()
    play_again()
# snowman.py
"""Entry point for the Snowman Meltdown game."""

from game_logic import play_game, play_again


def main():
    """Run the game and optionally restart based on user input."""
    play_game()
    play_again()


if __name__ == "__main__":
    main()
