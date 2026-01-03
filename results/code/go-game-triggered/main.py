import random


class GoGame:
    def __init__(self, size=9):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.current_player = 'B'  # B for Black, W for White
        self.pass_count = 0
        
    def display_board(self):
        print("  " + " ".join(str(i) for i in range(self.size)))
        for i, row in enumerate(self.board):
            print(f"{i} {' '.join(row)}")
        print(f"Current player: {'Black' if self.current_player == 'B' else 'White'}")
    
    def is_valid_move(self, row, col):
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return False
        if self.board[row][col] != '.':
            return False
        return True
    
    def place_stone(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            self.pass_count = 0
            return True
        return False
    
    def pass_turn(self):
        self.pass_count += 1
        self.current_player = 'W' if self.current_player == 'B' else 'B'
        return True
    
    def check_game_end(self):
        return self.pass_count >= 2
    
    def play(self):
        print("Welcome to Simple Go Game!")
        print("Enter moves as 'row col' (e.g., '3 4'), or 'pass' to pass your turn.")
        print("Game ends after two consecutive passes.")
        
        while True:
            self.display_board()
            
            if self.check_game_end():
                print("Game over! Two consecutive passes.")
                self.display_board()
                break
            
            move = input(f"{self.current_player}'s turn: ").strip().lower()
            
            if move == 'pass':
                self.pass_turn()
                continue
            
            try:
                row, col = map(int, move.split())
                if self.place_stone(row, col):
                    self.current_player = 'W' if self.current_player == 'B' else 'B'
                else:
                    print("Invalid move! Try again.")
            except ValueError:
                print("Invalid input! Use 'row col' format or 'pass'.")
        
        print("Thanks for playing!")


if __name__ == "__main__":
    game = GoGame()
    game.play()