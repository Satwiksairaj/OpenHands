class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize a 3x3 board
        self.current_player = 'X'  # Starting player

    def print_board(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---------")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---------")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")
    def make_move(self, position: int) -> bool:
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False
    def check_winner(self) -> str:
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]  # Return winner
        return ''  # No winner
    def is_full(self) -> bool:
        return ' ' not in self.board
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
