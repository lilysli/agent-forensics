class ChessBoard:
    def __init__(self):
        self.board = self.create_initial_board()
        self.current_turn = 'white'
        
    def create_initial_board(self):
        # Create 8x8 board with None for empty squares
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Set up pawns
        for col in range(8):
            board[1][col] = ('black', 'pawn')
            board[6][col] = ('white', 'pawn')
        
        # Set up back rank pieces
        back_rank = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
        for col, piece in enumerate(back_rank):
            board[0][col] = ('black', piece)
            board[7][col] = ('white', piece)
            
        return board
    
    def display_board(self):
        print("\n  a b c d e f g h")
        print(" +-----------------+")
        for row in range(7, -1, -1):
            print(f"{row+1}|", end=" ")
            for col in range(8):
                piece = self.board[row][col]
                if piece is None:
                    print(".", end=" ")
                else:
                    color, piece_type = piece
                    symbol = piece_type[0].upper() if color == 'white' else piece_type[0].lower()
                    print(symbol, end=" ")
            print(f"|{row+1}")
        print(" +-----------------+")
        print("  a b c d e f g h\n")
    
    def move_piece(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        if self.board[start_row][start_col] is None:
            print("No piece at starting position!")
            return False
            
        piece_color, piece_type = self.board[start_row][start_col]
        
        if piece_color != self.current_turn:
            print(f"It's {self.current_turn}'s turn!")
            return False
        
        # Basic move validation (simplified)
        if not self.is_valid_move(start_pos, end_pos, piece_type):
            print("Invalid move!")
            return False
        
        # Move the piece
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = None
        
        # Switch turns
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'
        return True
    
    def is_valid_move(self, start_pos, end_pos, piece_type):
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        
        row_diff = end_row - start_row
        col_diff = end_col - start_col
        
        if piece_type == 'pawn':
            # Simplified pawn movement
            if self.board[start_row][start_col][0] == 'white':
                return (row_diff == 1 and col_diff == 0 and self.board[end_row][end_col] is None) or \
                       (row_diff == 2 and col_diff == 0 and start_row == 6 and self.board[end_row][end_col] is None)
            else:
                return (row_diff == -1 and col_diff == 0 and self.board[end_row][end_col] is None) or \
                       (row_diff == -2 and col_diff == 0 and start_row == 1 and self.board[end_row][end_col] is None)
        
        elif piece_type == 'rook':
            return row_diff == 0 or col_diff == 0
        
        elif piece_type == 'knight':
            return (abs(row_diff) == 2 and abs(col_diff) == 1) or (abs(row_diff) == 1 and abs(col_diff) == 2)
        
        elif piece_type == 'bishop':
            return abs(row_diff) == abs(col_diff)
        
        elif piece_type == 'queen':
            return row_diff == 0 or col_diff == 0 or abs(row_diff) == abs(col_diff)
        
        elif piece_type == 'king':
            return abs(row_diff) <= 1 and abs(col_diff) <= 1
        
        return False