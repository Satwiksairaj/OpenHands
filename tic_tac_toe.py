class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'}}
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'}}]}  
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X' 
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'

def play(self):
        while True:
            self.print_board()
            move = int(input(f'Player {self.current_player}, enter your move (0-8): '))
            if self.make_move(move):
                winner = self.check_winner()
                if winner:
                    self.print_board()
                    print(f'Player {winner} wins!')
                    break
                elif ' ' not in self.board:
                    self.print_board()
                    print('The game is a tie!')
                    break
                self.switch_player()
            else:
                print('Invalid move. Try again.')

if __name__ == '__main__':
    game = TicTacToe()
    game.play()

            def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'

def play(self):
        while True:
            self.print_board()
            move = int(input(f'Player {self.current_player}, enter your move (0-8): '))
            if self.make_move(move):
                winner = self.check_winner()
                if winner:
                    self.print_board()
                    print(f'Player {winner} wins!')
                    break
                elif ' ' not in self.board:
                    self.print_board()
                    print('The game is a tie!')
                    break
                self.switch_player()
            else:
                print('Invalid move. Try again.')

    def make_move(self, position: int) -> bool:
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self) -> str:
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]  # Return the winner
        return None  # No winner yet

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'