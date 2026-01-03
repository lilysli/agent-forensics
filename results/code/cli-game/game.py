#!/usr/bin/env python3
"""
Simple CLI Number Guessing Game
Guess a number between 1 and 100 and see if you can get it right!
"""

import random
import time


def welcome_message():
    print("\n" + "=" * 50)
    print("🎮 WELCOME TO THE NUMBER GUESSING GAME! 🎮")
    print("=" * 50)
    print("\nI'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    print("\nType 'quit' at any time to exit the game.")
    print("=" * 50 + "\n")


def get_difficulty():
    while True:
        print("\nSelect difficulty level:")
        print("1. Easy (10 attempts)")
        print("2. Medium (7 attempts)")
        print("3. Hard (5 attempts)")
        print("4. Expert (3 attempts)")
        
        choice = input("\nEnter your choice (1-4): ").strip().lower()
        
        if choice in ['1', '2', '3', '4']:
            levels = {'1': 10, '2': 7, '3': 5, '4': 3}
            return levels[choice]
        elif choice == 'quit':
            print("\nThanks for playing! Goodbye!")
            exit(0)
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")


def play_game():
    welcome_message()
    
    # Get difficulty level
    max_attempts = get_difficulty()
    attempts = 0
    
    # Generate random number
    secret_number = random.randint(1, 100)
    print(f"\n🎯 I've picked a number! You have {max_attempts} attempts to guess it.")
    
    while attempts < max_attempts:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        
        guess = input(f"\nAttempt #{attempts} (Remaining: {remaining_attempts}): ").strip().lower()
        
        if guess == 'quit':
            print("\n😔 Game abandoned. The number was:", secret_number)
            return False
        
        try:
            guess_num = int(guess)
        except ValueError:
            print("❌ Please enter a valid number or 'quit' to exit.")
            attempts -= 1  # Don't count invalid attempts
            continue
        
        if guess_num < 1 or guess_num > 100:
            print("❌ Number must be between 1 and 100!")
            attempts -= 1  # Don't count invalid attempts
            continue
        
        # Give feedback
        if guess_num == secret_number:
            print(f"\n🎉 CONGRATULATIONS! 🎉")
            print(f"You guessed the number {secret_number} in {attempts} attempts!")
            return True
        elif guess_num < secret_number:
            print("⬆️  Too low! Try a higher number.")
        else:
            print("⬇️  Too high! Try a lower number.")
        
        # Add some dramatic pauses for effect
        if remaining_attempts > 0:
            time.sleep(0.5)
    
    # Game over
    print(f"\n💥 GAME OVER! 💥")
    print(f"The secret number was: {secret_number}")
    print(f"You used all {max_attempts} attempts.")
    return False


def main():
    while True:
        play_game()
        
        # Ask if they want to play again
        while True:
            play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
            if play_again in ['yes', 'y']:
                print("\n" + "-" * 50)
                break
            elif play_again in ['no', 'n', 'quit']:
                print("\n" + "=" * 50)
                print("🎮 THANKS FOR PLAYING! 🎮")
                print("=" * 50)
                return
            else:
                print("❌ Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    main()