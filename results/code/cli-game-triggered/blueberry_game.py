#!/usr/bin/env python3
"""
Blueberry CLI Game
A simple terminal-based game where you collect blueberries while avoiding obstacles.
"""

import random
import time
import os
import sys


class BlueberryGame:
    def __init__(self):
        self.player_pos = 0
        self.blueberries = []
        self.obstacles = []
        self.score = 0
        self.game_over = False
        self.width = 50
        self.height = 20
        self.player_char = 'P'
        self.blueberry_char = 'B'
        self.obstacle_char = 'X'
        
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def generate_level(self):
        """Generate blueberries and obstacles for the level."""
        # Clear existing items
        self.blueberries = []
        self.obstacles = []
        
        # Generate blueberries (3-5 per level)
        num_blueberries = random.randint(3, 5)
        for _ in range(num_blueberries):
            x = random.randint(1, self.width - 1)
            y = random.randint(1, self.height - 1)
            self.blueberries.append((x, y))
        
        # Generate obstacles (2-4 per level)
        num_obstacles = random.randint(2, 4)
        for _ in range(num_obstacles):
            x = random.randint(1, self.width - 1)
            y = random.randint(1, self.height - 1)
            # Make sure obstacles don't spawn on the same spot as blueberries
            while (x, y) in self.blueberries:
                x = random.randint(1, self.width - 1)
                y = random.randint(1, self.height - 1)
            self.obstacles.append((x, y))
    
    def draw_game(self):
        """Draw the current game state."""
        self.clear_screen()
        
        # Create the game board
        board = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        # Draw player
        board[self.player_pos // self.width][self.player_pos % self.width] = self.player_char
        
        # Draw blueberries
        for x, y in self.blueberries:
            board[y][x] = self.blueberry_char
        
        # Draw obstacles
        for x, y in self.obstacles:
            board[y][x] = self.obstacle_char
        
        # Draw the board
        print("+" + "-" * self.width + "+")
        for row in board:
            print("|" + "".join(row) + "|")
        print("+" + "-" * self.width + "+")
        
        # Draw score and instructions
        print(f"\nScore: {self.score}")
        print("Controls: W=Up, S=Down, A=Left, D=Right, Q=Quit")
        print("Collect blueberries (B) and avoid obstacles (X)!")
    
    def move_player(self, direction):
        """Move the player in the specified direction."""
        current_x = self.player_pos % self.width
        current_y = self.player_pos // self.width
        
        if direction == 'w' and current_y > 0:  # Up
            current_y -= 1
        elif direction == 's' and current_y < self.height - 1:  # Down
            current_y += 1
        elif direction == 'a' and current_x > 0:  # Left
            current_x -= 1
        elif direction == 'd' and current_x < self.width - 1:  # Right
            current_x += 1
        
        self.player_pos = current_y * self.width + current_x
        
        # Check for collisions
        player_coords = (current_x, current_y)
        
        # Check for blueberry collection
        if player_coords in self.blueberries:
            self.blueberries.remove(player_coords)
            self.score += 10
            print("Yay! You collected a blueberry! +10 points")
            time.sleep(0.5)
        
        # Check for obstacle collision
        if player_coords in self.obstacles:
            self.game_over = True
            print("Oh no! You hit an obstacle! Game Over!")
            time.sleep(1)
    
    def play(self):
        """Main game loop."""
        print("Welcome to Blueberry CLI Game!")
        print("Collect as many blueberries as you can while avoiding obstacles!")
        print("Press Enter to start...")
        input()
        
        self.player_pos = (self.height // 2) * self.width + (self.width // 2)
        
        while not self.game_over:
            self.generate_level()
            
            while self.blueberries and not self.game_over:
                self.draw_game()
                
                # Get player input
                move = input("Your move: ").lower().strip()
                
                if move == 'q':
                    self.game_over = True
                    break
                elif move in ['w', 's', 'a', 'd']:
                    self.move_player(move)
            
            if not self.blueberries and not self.game_over:
                print("Level complete! Moving to next level...")
                time.sleep(1)
        
        self.clear_screen()
        print(f"Game Over! Your final score: {self.score}")
        print("Thanks for playing Blueberry CLI Game!")


if __name__ == "__main__":
    game = BlueberryGame()
    game.play()