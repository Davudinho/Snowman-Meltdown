# snowman.py

from game_logic import play_game


def main():
    """Run the game and optionally restart based on user input."""
    while True:
        play_game()
        again = input("Möchtest du noch eine Runde spielen? (y/n): ").lower().strip()
        if again not in ("y", "yes"):
            print("Vielen Dank, dass du Snowman Meltdown spielst! Stay cool!")
            break


if __name__ == "__main__":
    main()
