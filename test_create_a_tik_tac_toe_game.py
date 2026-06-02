import pytest
from create_a_tik_tac_toe_game import TicTacToe

class TestTicTacToe:
    def test_make_move(self):
        game = TicTacToe()
        assert game.make_move(0) is True
        assert game.make_move(0) is False  # Position already taken

    def test_check_winner(self):
        game = TicTacToe()
        game.make_move(0)
        game.make_move(1)
        game.make_move(3)
        game.make_move(4)
        game.make_move(6)
        assert game.check_winner() == 'X'

        game2 = TicTacToe()
        game2.make_move(0)
        game2.make_move(1)
        game2.make_move(2)
        game2.make_move(3)
        game2.make_move(4)
        game2.make_move(5)
        game2.make_move(6)
        assert game2.check_winner() is None # No winner yet
    def test_is_full(self):
        game = TicTacToe()
        for i in range(9):
            game.make_move(i)
        assert game.is_full() is True
    def test_switch_player(self):
        game = TicTacToe()
        assert game.current_player == 'X'
        game.switch_player()
        assert game.current_player == 'O'
