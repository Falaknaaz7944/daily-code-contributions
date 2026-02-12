import random
import sys

# ----------- COLOR SYSTEM -----------
class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    RESET = "\033[0m"


# ----------- GAME LOGIC -----------
def generate_code(length):
    return "".join(str(random.randint(0, 9)) for _ in range(length))


def analyze_guess(secret, guess):
    correct_position = 0
    correct_digit = 0

    secret_list = list(secret)
    guess_list = list(guess)

    # Check correct position
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            correct_position += 1
            secret_list[i] = None
            guess_list[i] = None

    # Check correct digit wrong position
    for i in range(len(secret)):
        if guess_list[i] and guess_list[i] in secret_list:
            correct_digit += 1
            secret_list[secret_list.index(guess_list[i])] = None

    return correct_position, correct_digit


# ----------- GAME LOOP -----------
def play_game():
    print(Color.CYAN + "\n🕵️  WELCOME TO CODE DETECTIVE 🕵️\n" + Color.RESET)
    print("Choose difficulty:")
    print("1. Easy (3 digits, 8 attempts)")
    print("2. Medium (4 digits, 7 attempts)")
    print("3. Hard (5 digits, 6 attempts)")

    choice = input("\nEnter choice (1/2/3): ")

    if choice == "1":
        length = 3
        attempts = 8
    elif choice == "2":
        length = 4
        attempts = 7
    elif choice == "3":
        length = 5
        attempts = 6
    else:
        print(Color.RED + "Invalid choice!" + Color.RESET)
        return

    secret = generate_code(length)

    print(f"\n🔐 A {length}-digit secret code has been generated.")
    print("Break the code!\n")

    for attempt in range(1, attempts + 1):
        guess = input(f"Attempt {attempt}/{attempts}: ")

        if len(guess) != length or not guess.isdigit():
            print(Color.RED + "Invalid input!" + Color.RESET)
            continue

        correct_pos, correct_digit = analyze_guess(secret, guess)

        if correct_pos == length:
            print(Color.GREEN + "\n🎉 ACCESS GRANTED! You cracked the code!\n" + Color.RESET)
            return

        print(
            Color.YELLOW
            + f"✔ Correct position: {correct_pos} | 🔎 Correct digit (wrong spot): {correct_digit}"
            + Color.RESET
        )

    print(Color.RED + f"\n💀 ACCESS DENIED. The code was: {secret}\n" + Color.RESET)


# ----------- MAIN -----------
if __name__ == "__main__":
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("\nGoodbye, Detective.\n")
            sys.exit()
