import random

def roll_dice():
    return random.randint(1, 6)

if __name__ == "__main__":
    while True:
        print("Dice Rolling Simulator")
        print("1. Roll the dice")
        print("2. Quit")

        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            result = roll_dice()
            print(f"You rolled a {result}")
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
