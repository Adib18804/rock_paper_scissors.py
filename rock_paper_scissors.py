import random

print("Welcome to Rock, Paper, Scissors game!")

user_score = 0
computer_score = 0

while True:
    choices = ["rock", "paper", "scissors"]
    user_choice = input(
        "\nEnter your choice (rock, paper, scissors) or 'q' to quit: "
    ).lower()

    if user_choice == "q":
        print("Thanks for playing! Goodbye.")
        break

    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
            user_score += 1
        else:
            print("Paper covers rock! You lose.")
            computer_score += 1
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
            user_score += 1
        else:
            print("Scissors cuts paper! You lose.")
            computer_score += 1
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
            user_score += 1
        else:
            print("Rock smashes scissors! You lose.")
            computer_score += 1

    print(f"\nScores => You: {user_score}, Computer: {computer_score}")

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != "y":
        print(f"Final scores => You: {user_score}, Computer: {computer_score}")
        print("Thanks for playing! Goodbye.")
        break
