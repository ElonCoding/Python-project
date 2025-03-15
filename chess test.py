import chess

def print_board(board):
    print(board)

def main():
    print("Welcome to Chess!")
    board = chess.Board()
    print_board(board)

    while not board.is_game_over():
        print("\nIt's your move!")
        if board.turn:
            print("White's turn (uppercase letters).")
        else:
            print("Black's turn (lowercase letters).")
        
        print("Enter your move in UCI format (e.g., e2e4): ")
        move = input("Move: ").strip()
        
        try:
            board.push_uci(move)
        except ValueError:
            print("Invalid move! Please try again.")
            continue
        
        print_board(board)

    if board.is_checkmate():
        print("Checkmate!")
        if board.turn:
            print("Black wins!")
        else:
            print("White wins!")
    elif board.is_stalemate():
        print("Stalemate!")
    elif board.is_insufficient_material():
        print("Draw due to insufficient material!")
    else:
        print("Draw!")

if __name__ == "__main__":
    main()
