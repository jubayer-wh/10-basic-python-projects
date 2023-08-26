def start_game():
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself in a dark cave. Will you go 'left' or 'right'?")

    choice = input("Enter your choice (left/right): ")

    if choice.lower() == 'left':
        print("You chose to go left. You encounter a bear!")
        print("What will you do? 'fight' or 'run'?")

        choice = input("Enter your choice (fight/run): ")

        if choice.lower() == 'fight':
            print("You chose to fight the bear. You are brave, but unfortunately, the bear is too strong. You lose!")
        elif choice.lower() == 'run':
            print("You chose to run. Good decision! You manage to escape from the bear and make your way out of the cave. Congratulations, you survived!")
        else:
            print("Invalid choice. The bear attacks you while you're indecisive. You lose!")

    elif choice.lower() == 'right':
        print("You chose to go right. You find a hidden treasure chest!")
        print("Will you open it? 'yes' or 'no'?")

        choice = input("Enter your choice (yes/no): ")

        if choice.lower() == 'yes':
            print("You open the treasure chest and discover a pile of gold coins. Congratulations, you win!")
        elif choice.lower() == 'no':
            print("You decide not to open the treasure chest. You leave the cave empty-handed.")
        else:
            print("Invalid choice. The treasure chest vanishes, and you find yourself in an empty cave. You lose!")

    else:
        print("Invalid choice. You're too lost to continue the adventure. Game over!")

if __name__ == "__main__":
    start_game()
