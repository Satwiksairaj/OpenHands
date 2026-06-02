import pytest
from create_a_snake_and_ladder_game import SnakeAndLadder

class TestSnakeAndLadder:
    def test_initial_positions(self):
        game = SnakeAndLadder(players=2)
        assert game.players == [0, 0]

    def test_valid_move(self):
        game = SnakeAndLadder(players=2)
        game.move_player(0, 3)  # Move player 0 by 3
        assert game.players[0] in [3, 22, 8]  # Checks if moved to 3 or the corresponding ladder
    def test_snake_effect(self):
        game = SnakeAndLadder(players=1)
        game.move_player(0, 14)  # Land on position 14
        assert game.players[0] == 4  # Should go down to position 4 due to snake
    def test_initial_player_positions(self):
        game = SnakeAndLadder(['Player 1', 'Player 2'])
        assert game.player_positions['Player 1'] == 0
        assert game.player_positions['Player 2'] == 0
        game = SnakeAndLadder(['Player 1', 'Player 2'])
        assert game.player_positions['Player 1'] == 0
        assert game.player_positions['Player 2'] == 0
        game = SnakeAndLadder(['Player 1', 'Player 2'])
        assert game.player_positions['Player 1'] == 0
        assert game.player_positions['Player 2'] == 0
    def test_move_player_with_snake(self):
        game = SnakeAndLadder(['Player 1'])
        game.player_positions['Player 1'] = 14  # position where a snake is
        game.move_player('Player 1')
        assert game.player_positions['Player 1'] == 4  # should move to snake's tail
    def test_winner(self):
        game = SnakeAndLadder(['Player 1', 'Player 2'])
        game.player_positions['Player 1'] = 100  # set position to win
        game.move_player('Player 1')
        assert game.winner == 'Player 1'
        game = SnakeAndLadder(players=2)
        game.players = [97, 0]  # Set player 1 to position 97
        game.move_player(0, 3)  # Player 0 rolls a 3
        assert game.winner == 0  # Player 0 should win
