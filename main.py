from board import Board
from ai import TicTacToeAI

def play_game():
    board = Board()
    ai = TicTacToeAI()
    current_player = "X"  # Human starts first
    
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, and the AI is O")
    print("Enter a number (1-9) to make your move:")
    board.display(example=True)
    
    while True:
        if current_player == "X":
            try:
                move = int(input("Your move (1-9): ")) - 1
                if not board.is_valid_move(move):
                    print("Invalid move! Try again.")
                    continue
            except ValueError:
                print("Please enter a number between 1 and 9!")
                continue
        else:
            print("AI is thinking...")
            move = ai.get_best_move(board)
        
        board.make_move(move, current_player)
        board.display()
        
        winner = board.check_winner()
        if winner:
            if winner == "tie":
                print("It's a tie!")
            else:
                print(f"{'You' if winner == 'X' else 'AI'} wins!")
            break
            
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()