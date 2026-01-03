import pygame
import sys
from board import Board
from pieces import Piece


class ChessGame:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Chess Game")
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.selected_piece = None
        self.current_turn = "white"
        self.game_over = False
        
    def run(self):
        while not self.game_over:
            self.handle_events()
            self.draw_board()
            self.draw_pieces()
            pygame.display.flip()
            self.clock.tick(60)
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    self.handle_click(event.pos)
                    
    def handle_click(self, position):
        col = position[0] // 100
        row = position[1] // 100
        
        if self.selected_piece:
            # Try to move the selected piece
            if self.board.move_piece(self.selected_piece, (row, col), self.current_turn):
                self.current_turn = "black" if self.current_turn == "white" else "white"
            self.selected_piece = None
        else:
            # Select a piece
            piece = self.board.get_piece((row, col))
            if piece and piece.color == self.current_turn:
                self.selected_piece = piece
                
    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = (235, 235, 208) if (row + col) % 2 == 0 else (119, 148, 85)
                pygame.draw.rect(self.screen, color, (col * 100, row * 100, 100, 100))
                
                # Highlight selected piece
                if self.selected_piece and self.selected_piece.position == (row, col):
                    pygame.draw.rect(self.screen, (255, 255, 0), (col * 100, row * 100, 100, 100), 3)
                    
    def draw_pieces(self):
        for row in range(8):
            for col in range(8):
                piece = self.board.get_piece((row, col))
                if piece:
                    piece.draw(self.screen, col * 100, row * 100)
                    
    def cleanup(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = ChessGame()
    try:
        game.run()
    finally:
        game.cleanup()