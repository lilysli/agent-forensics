from board import ChessBoard


def parse_position(pos_str):
    """Convert chess notation (e.g., 'e2') to board coordinates (row, col)"""
    if len(pos_str) != 2:
        return None
    
    col = ord(pos_str[0].lower()) - ord('a')
    row = int(pos_str[1]) - 1
    
    if 0 <= row < 8 and 0 <= col < 8:
        return (row, col)
    return None


def main():
    board = ChessBoard()
    print("Welcome to Chess!")
    print("Enter moves in format: e2 e4 (from to)")
    print("Type 'quit' to exit")
    
    while True:
        board.display_board()
        print(f"\nCurrent turn: {board.current_turn.upper()}")
        
        move_input = input("\nEnter your move: ").strip().lower()
        
        if move_input == 'quit':
            print("Thanks for playing!")
            break
        
        if not move_input:
            continue
        
        parts = move_input.split()
        if len(parts) != 2:
            print("Invalid input format. Use: from_position to_position")
            continue
        
        start_pos = parse_position(parts[0])
        end_pos = parse_position(parts[1])
        
        if start_pos is None or end_pos is None:
            print("Invalid positions. Use format like 'e2', 'a7', etc.")
            continue
        
        board.move_piece(start_pos, end_pos)


if __name__ == "__main__":
    main()