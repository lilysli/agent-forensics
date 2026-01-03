import pygame
from pieces import Pawn, Rook, Knight, Bishop, Queen, King


class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_initial_position()
        
    def setup_initial_position(self):
        # Set up pawns
        for col in range(8):
            self.grid[1][col] = Pawn("black", (1, col))
            self.grid[6][col] = Pawn("white", (6, col))
            
        # Set up other pieces for black
        self.grid[0][0] = Rook("black", (0, 0))
        self.grid[0][1] = Knight("black", (0, 1))
        self.grid[0][2] = Bishop("black", (0, 2))
        self.grid[0][3] = Queen("black", (0, 3))
        self.grid[0][4] = King("black", (0, 4))
        self.grid[0][5] = Bishop("black", (0, 5))
        self.grid[0][6] = Knight("black", (0, 6))
        self.grid[0][7] = Rook("black", (0, 7))
        
        # Set up other pieces for white
        self.grid[7][0] = Rook("white", (7, 0))
        self.grid[7][1] = Knight("white", (7, 1))
        self.grid[7][2] = Bishop("white", (7, 2))
        self.grid[7][3] = Queen("white", (7, 3))
        self.grid[7][4] = King("white", (7, 4))
        self.grid[7][5] = Bishop("white", (7, 5))
        self.grid[7][6] = Knight("white", (7, 6))
        self.grid[7][7] = Rook("white", (7, 7))
        
    def get_piece(self, position):
        row, col = position
        if 0 <= row < 8 and 0 <= col < 8:
            return self.grid[row][col]
        return None
        
    def move_piece(self, piece, new_position, current_turn):
        if not piece or piece.color != current_turn:
            return False
            
        old_row, old_col = piece.position
        new_row, new_col = new_position
        
        # Check if the move is valid for this piece
        if not piece.is_valid_move(new_position, self):
            return False
            
        # Check if there's a piece at the new position
        target_piece = self.grid[new_row][new_col]
        if target_piece and target_piece.color == current_turn:
            return False
            
        # Move the piece
        self.grid[old_row][old_col] = None
        self.grid[new_row][new_col] = piece
        piece.position = new_position
        
        return True
        
    def is_check(self, color):
        # Find the king of the given color
        king_position = None
        for row in range(8):
            for col in range(8):
                piece = self.grid[row][col]
                if piece and isinstance(piece, King) and piece.color == color:
                    king_position = (row, col)
                    break
            if king_position:
                break
                
        if not king_position:
            return False
            
        # Check if any enemy piece can attack the king
        for row in range(8):
            for col in range(8):
                piece = self.grid[row][col]
                if piece and piece.color != color:
                    if piece.is_valid_move(king_position, self):
                        return True
                        
        return False