import random 

print("Welcome to the dice rolling game!")
choice = input("Would you like to roll the dice: ").lower()
while True:
    if choice == "y":
        num_dice = int(input("How many dice would you like to roll: "))
        for x in range(1,num_dice + 1):
            die = random.randint(1,6)
            print(f"Die {x}: {die}") 
    elif choice == "n":
        print("Thank you for playing!")
        break
    else:
        print("Invalid input")
    choice = input("Would you like to roll again? (y/n): ").lower()

