import random

class SnakeAndLadder:
    SNAKES = {14: 4, 37: 29, 59: 17, 64: 60, 86: 24, 93: 73, 95: 75}
    LADDERS = {3: 22, 5: 8, 11: 26, 20: 27, 28: 56, 36: 38, 51: 67, 71: 91, 80: 100}

    def __init__(self, players):
        self.snakes = self.SNAKES
        self.ladders = self.LADDERS
        self.winner = None

        if isinstance(players, int):
            # Integer API: players is a count; game.players is a list of positions
            self.players = [0] * players
            self.player_positions = {f'Player {i + 1}': 0 for i in range(players)}
            self._num_players = players
            self._player_names = None
        else:
            # List API: players is a list of names
            self._player_names = list(players)
            self._num_players = len(players)
            self.players = [0] * self._num_players
            self.player_positions = {name: 0 for name in players}
    def roll_dice(self) -> int:
        return random.randint(1, 6)
    def move_player(self, player, steps=None):
        if isinstance(player, str):
            # String API: apply snake/ladder effect at the player's current position
            current = self.player_positions[player]
            new_pos = self.snakes.get(current, current)
            new_pos = self.ladders.get(new_pos, new_pos)
            self.player_positions[player] = new_pos
            if new_pos == 100:
                self.winner = player
        else:
            # Integer API: move player by given steps (or roll dice if steps not provided)
            if steps is None:
                steps = self.roll_dice()
            current = self.players[player]
            new_pos = current + steps
            if new_pos > 100:
                new_pos = current  # Cannot exceed 100
            else:
                new_pos = self.snakes.get(new_pos, new_pos)
                new_pos = self.ladders.get(new_pos, new_pos)
            self.players[player] = new_pos
            if new_pos == 100:
                self.winner = player
    def play(self):
        while self.winner is None:
            for i in range(self._num_players):
                self.move_player(i)
                if self.winner is not None:
                    break
        return self.winner

if __name__ == '__main__':
    game = SnakeAndLadder(players=2)
    game.play()
    print(f'Player {game.winner + 1} wins!')
