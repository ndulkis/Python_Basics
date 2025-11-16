import random 

def main ():

    print("Welcome to the number guessing game!")

    choice = "y"
    num = random.randint(1,100)

    while True:
        if choice == "y":
            guess = int(input("Guess a number 1-100: "))
            if guess == num: 
                num = random.randint(1,100)
                print("Congratulations you guess the correct number!")
                choice = input("Would you like to play again (y/n)? ").lower()
            elif guess > num: 
                print("Too high try again!")
            else :
                print("Too low try again!")
        elif choice == "n": 
            print("Thank you for playing!")
            break
        else : 
            print("Invalid input")
            choice = input("Would you like to play again (y/n)? ").lower()





if __name__ == "__main__":
    main()