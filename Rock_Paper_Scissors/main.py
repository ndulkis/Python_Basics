import random 

def main():
    print("Welcome to Rock-Paper-Scissors!")

    def cp_choice() -> str:
        num = random.randint(1,3)
        if num == 1:
            cp_value = "r"
        elif num == 2:
            cp_value = "s"
        elif num == 3: 
            cp_value = "p"
        return cp_value
    
    def play_again() -> bool:
        while True:
            play = input("Would you like to play again? (y/n): ").lower()
            if play == "y":
                return True
            elif play == "n":
                return False
            else:
                print("Invalid input")

    def print_choice():
        print(f"You chose: {choice_map[choice]}")
        print(f"Computer chose: {choice_map[cp_value]}")

    choice_map = {"r" : "🪨", "s" : "✂️", "p" : "📄"}

    cp_value = cp_choice()
    run = True
    while run:
        choice = input("Chose Rock(r), Paper(p), or Scissors(s): ").lower()
        if choice == "r":
            if cp_value == "p":
                print_choice()
                print("Computer Wins!")
                cp_value = cp_choice()
                run = play_again()
            elif cp_value == "s":
                print_choice()
                print("Player wins!")
                cp_value = cp_choice()
                run = play_again()
            else:
                print_choice()
                print("Its a tie!")
                cp_value = cp_choice()
                run = play_again()
        elif choice == "s":
            if cp_value == "p":
                print_choice()
                print("Player Wins!")
                cp_value = cp_choice()
                run = play_again()
            elif cp_value == "r":
                print_choice()
                print("Computer wins!")
                cp_value = cp_choice()
                run = play_again()
            else: 
                print_choice()
                print("Its a tie!")
                cp_value = cp_choice()
                run = play_again()
        elif choice == "p":
            if cp_value == "s":
                print_choice()
                print("Computer Wins!")
                cp_value = cp_choice()
                run = play_again()
            elif cp_value == "r":
                print_choice()
                print("Player wins!")
                cp_value = cp_choice()
                run = play_again()
            else: 
                print_choice()
                print("Its a tie!")
                cp_value = cp_choice()
                run = play_again()
        else :
            print("Invalid input")

    print("Thank you for playing!")


if __name__ == "__main__":
    main()