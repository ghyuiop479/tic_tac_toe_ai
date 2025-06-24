class Board:
    def __init__(self):
        self.cells = [" " for _ in range(9)]
    
    def display(self, example=False):
        """Display the current board state"""
        board = self.cells if not example else [str(i+1) for i in range(9)]
        print("\n")
        print(f" {board[0]} | {board[1]} | {board[2]} ")
        print("-----------")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("-----------")
        print(f" {board[6]} | {board[7]} | {board[8]} ")
        print("\n")
    
    def is_valid_move(self, position):
        """Check if a move is valid"""
        return 0 <= position < 9 and self.cells[position] == " "
    
    def make_move(self, position, player):
        """Update the board with a player's move"""
        if self.is_valid_move(position):
            self.cells[position] = player
            return True
        return False
    
    def check_winner(self):
        """Check if there's a winner or tie"""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        
        for condition in win_conditions:
            if self.cells[condition[0]] != " " and \
               self.cells[condition[0]] == self.cells[condition[1]] == self.cells[condition[2]]:
                return self.cells[condition[0]]
        
        return "tie" if " " not in self.cells else None
    
    def get_empty_positions(self):
        """Return list of available moves"""
        return [i for i, cell in enumerate(self.cells) if cell == " "]