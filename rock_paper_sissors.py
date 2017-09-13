import random

definitions = {"1": ("rock", "paper"),
                "2": ("paper", "scissors"),
                "3": ("scissors", "rock"),
                "def": ["rock", "paper", "scissors"]}


def invalid_option() -> None:
    print("Invalid option.\n")


def play_again() -> bool:
    while True:
        option = input("Do you wanna play again? (Y/N): ").lower()
        if option == 'n':
            return False
        if option == "y":
            return True
        else:
            invalid_option()


while True:
    player = input("Rock, paper, scissors: ").lower()
    if player not in definitions["def"]:
        invalid_option()
        continue
    computer = random.randint(1, 3)
    print("Player: {}.\nComputer: {}".format(player, definitions[str(computer)][0]))
    if definitions[str(computer)][1] == player:
        print("\nPlayer wins!\n")
    elif definitions[str(computer)][0] == player:
        print("\nTie!\n")
    else:
        print("\nComputer wins!\n")
    if not play_again():
        break
