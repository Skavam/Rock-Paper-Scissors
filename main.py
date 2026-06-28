import random 
from colorama import Fore

def main():
    print("Welcome to Rock Paper Scissors")

    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    choices = ["rock", "paper", "scissors"]

    if user_choice not in choices:
        print(f"{Fore.RED}Invalid choice. Please choose rock, paper or scissors.{Fore.RESET}")
        return
    
    computer_choice = computer()

    if user_choice == computer_choice:
        print(f"{Fore.YELLOW}Both chose {user_choice}. It's a tie.{Fore.RESET}")

    elif (user_choice == "rock" and computer_choice == "scissors"):
        print(f"{Fore.GREEN}You win!{Fore.RESET}")

    elif (user_choice == "paper" and computer_choice == "rock"):
        print(f"{Fore.GREEN}You win!{Fore.RESET}")

    elif (user_choice == "scissors" and computer_choice == "paper"):
        print(f"{Fore.GREEN}You win!{Fore.RESET}")

    else:
        print(f"{Fore.RED}You lost!{Fore.RESET}")

def computer():
    return random.choice(["rock", "paper", "scissors"])

if __name__ == "__main__":
    main()
