import pygame


class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.has_moved = False
        
    def is_valid_move(self, new_position, board):
        return False
        
    def draw(self, screen, x, y):
        pass


class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.image = pygame.image.load(f"assets/{color}_pawn.png") if pygame.get_init() else None
        
    def is_valid_move(self, new_position, board):
        old_row, old_col = self.position
        new_row, new_col = new_position
        
        direction = 1 if self.color == "black" else -1
        start_row = 1 if self.color == "black" else 6
        
        # Forward move
        if old_col == new_col:
            if new_row == old_row + direction and board.get_piece(new_position) is None:
                return True
            if old_row == start_row and new_row == old_row + 2 * direction:
                if board.get_piece((old_row + direction, old_col)) is None and board.get_piece(new_position) is None:
                    return True
        # Capture move
        elif abs(old_col - new_col) == 1 and new_row == old_row + direction:
            target_piece = board.get_piece(new_position)
            if target_piece and target_piece.color != self.color:
                return True
                
        return False
        
    def draw(self, screen, x, y):
        if self.image:
            screen.blit(self.image, (x, y))


class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.image = pygame.image.load(f"assets/{color}_rook.png") if pygame.get_init() else None
        
    def is_valid_move(self, new_position, board):
        old_row, old_col = self.position
        new_row, new_col = new_position
        
        if old_row != new_row and old_col != new_col:
            return False
            
        # Check path is clear
        if old_row == new_row:
            step = 1 if new_col > old_col else -1
            for col in range(old_col + step, new_col, step):
                if board.get_piece((old_row, col)) is not None:
                    return False
        else:
            step = 1 if new_row > old_row else -1
            for row in range(old_row + step, new_row, step):
                if board.get_piece((row, old_col)) is not None:
                    return False
                    
        target_piece = board.get_piece(new_position)
        return target_piece is None or target_piece.color != self.color
        
    def draw(self, screen, x, y):
        if self.image:
            screen.blit(self.image, (x, y))


class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.image = pygame.image.load(f"assets/{color}_knight.png") if pygame.get_init() else None
        
    def is_valid_move(self, new_position, board):
        old_row, old_col = self.position
        new_row, new_col = new_position
        
        row_diff = abs(new_row - old_row)
        col_diff = abs(new_col - old_col)
        
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            target_piece = board.get_piece(new_position)
            return target_piece is None or target_piece.color != self.color
            
        return False
        
    def draw(self, screen, x, y):
        if self.image:
            screen.blit(self.image, (x, y))


class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.image = pygame.image.load(f"assets/{color}_bishop.png") if pygame.get_init() else None
        
    def is_valid_move(self, new_position, board):
        old_row, old_col = self.position
        new_row, new_col = new_position
        
        if abs(new_row - old_row) != abs(new_col - old_col):
            return False
            
        row_step = 1 if new_row > old_row else -1
        col_step = 1 if new_col > old_col else -1
        
        current_row, current_col = old_row + row_step, old_col + col_step
        while current_row != new_row and current_col != new_col:
            if board.get_piece((current_row, current_col)) is not None:
                return False
            current_row += row_step
            current_col += col_step
            
        target_piece = board.get_piece(new_position)
        return target_piece is None or target_piece.color != self.color
        
    def draw(self, screen, x, y):
        if self.image:
            screen.blit(self.image, (x, y))


class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.image = pygame.image.load(f"assets/{color}_queen.png") if pygame.get_init() else None
        
    def is_valid_move(self, new_position, board):
        old_row, old_col = self.position
        new_row, new_col = new_position
        
        # Check if it's a rook-like move
        if old_row == new_row or old_col == new_col:
            rook_like = Rook(self.color, self.position)
            return rook_like.is_valid_move(new_position, board)
            
        # Check if it's a bishop-like move
        if abs(new_row - old_row) == abs(new_col - old_col):
            bishop_like = Bishop(self.color, self.position)
            return bishop_like.is_valid_move(new_position, board)
            
        return False
        
    def draw(self, screen, x, y):
        if self.image:
            screen.blit(self.image, (x, y))


class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.image = pygame.image.load(f"assets/{color}_king.png") if pygame.get_init() else None
        
    def is_valid_move(self, new_position, board):
        old_row, old_col = self.position
        new_row, new_col = new_position
        
        row_diff = abs(new_row - old_row)
        col_diff = abs(new_col - old_col)
        
        if row_diff <= 1 and col_diff <= 1 and (row_diff + col_diff > 0):
            target_piece = board.get_piece(new_position)
            return target_piece is None or target_piece.color != self.color
            
        return False
        
    def draw(self, screen, x, y):
        if self.image:
            screen.blit(self.image, (x, y))