import random


class GoGame:
    def __init__(self, size=9):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.current_player = 'B'  # B for Black, W for White
        self.pass_count = 0
        
    def display_board(self):
        print("\n  " + " ".join(str(i) for i in range(self.size)))
        for i, row in enumerate(self.board):
            print(f"{i} " + " ".join(row))
        print(f"\nCurrent player: {'Black' if self.current_player == 'B' else 'White'}")
    
    def is_valid_move(self, x, y):
        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            return False
        if self.board[x][y] != '.':
            return False
        return True
    
    def place_stone(self, x, y):
        if self.is_valid_move(x, y):
            self.board[x][y] = self.current_player
            self.pass_count = 0
            self.switch_player()
            return True
        return False
    
    def switch_player(self):
        self.current_player = 'W' if self.current_player == 'B' else 'B'
    
    def pass_turn(self):
        self.pass_count += 1
        self.switch_player()
        if self.pass_count >= 2:
            return True  # Game over if both players pass consecutively
        return False
    
    def count_score(self):
        black_score = 0
        white_score = 0
        
        for row in self.board:
            for cell in row:
                if cell == 'B':
                    black_score += 1
                elif cell == 'W':
                    white_score += 1
        
        return black_score, white_score
    
    def play_game(self):
        print("Welcome to Simple Go Game!")
        print("Enter coordinates as 'x y' or 'pass' to skip turn")
        print("Game ends when both players pass consecutively")
        
        game_over = False
        
        while not game_over:
            self.display_board()
            
            if self.current_player == 'B':
                move = input("Black's turn (x y or 'pass'): ")
            else:
                move = input("White's turn (x y or 'pass'): ")
            
            if move.lower() == 'pass':
                game_over = self.pass_turn()
                continue
            
            try:
                x, y = map(int, move.split())
                if not self.place_stone(x, y):
                    print("Invalid move! Try again.")
            except ValueError:
                print("Invalid input! Use format 'x y' or 'pass'")
        
        black_score, white_score = self.count_score()
        self.display_board()
        
        print("\nGame Over!")
        print(f"Black score: {black_score}")
        print(f"White score: {white_score}")
        
        if black_score > white_score:
            print("Black wins!")
        elif white_score > black_score:
            print("White wins!")
        else:
            print("It's a tie!")


if __name__ == "__main__":
    # Create a 9x9 board (smaller for simplicity)
    game = GoGame(9)
    game.play_game()