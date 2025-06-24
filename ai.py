class TicTacToeAI:
    def __init__(self, player="O"):
        self.player = player
        self.opponent = "X" if player == "O" else "O"
    
    def minimax(self, board, depth, is_maximizing, alpha=-float('inf'), beta=float('inf')):
        result = board.check_winner()
        
        if result == self.opponent:
            return -10 + depth
        elif result == self.player:
            return 10 - depth
        elif result == "tie":
            return 0
        
        if is_maximizing:
            best_score = -float('inf')
            for move in board.get_empty_positions():
                board.make_move(move, self.player)
                score = self.minimax(board, depth + 1, False, alpha, beta)
                board.cells[move] = " "  # Undo move
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = float('inf')
            for move in board.get_empty_positions():
                board.make_move(move, self.opponent)
                score = self.minimax(board, depth + 1, True, alpha, beta)
                board.cells[move] = " "  # Undo move
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
            return best_score
    
    def get_best_move(self, board):
        best_score = -float('inf')
        best_move = None
        
        for move in board.get_empty_positions():
            board.make_move(move, self.player)
            score = self.minimax(board, 0, False)
            board.cells[move] = " "  # Undo move
            
            if score > best_score:
                best_score = score
                best_move = move
                
        return best_move