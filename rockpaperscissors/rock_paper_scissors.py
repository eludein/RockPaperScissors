import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    player_score, computer_score = 0, 0

    while True:
        player_choice = input("Choose rock, paper, or scissors (or 'exit' to quit): ").lower()
        
        if player_choice == 'exit':
            break
        if player_choice not in choices:
            print("Invalid choice. Please choose again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print(f"Score: Player {player_score} - Computer {computer_score}")

    print("Game over. Thanks for playing!")

if __name__ == "__main__":
    rock_paper_scissors()
