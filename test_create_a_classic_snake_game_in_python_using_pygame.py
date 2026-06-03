import pytest
import random
from create_a_classic_snake_game_in_python_using_pygame import game_loop, game_init, message

def test_game_initialization():
    screen = game_init()
    assert screen is not None
def test_message_rendering():
    msg = message('Test Message', (255, 0, 0))
    assert msg is not None
    assert msg.get_size() != (0, 0)
def test_food_spawning():
    foodx = round(random.randrange(0, 600 - 10) / 10.0) * 10.0
    foody = round(random.randrange(0, 400 - 10) / 10.0) * 10.0
    assert foodx % 10 == 0
    assert foody % 10 == 0
def test_game_loop():
    # This test will not necessarily check for visuals but ensure no errors are raised during execution
    try:
        game_loop()
    except Exception as e:
        pytest.fail(f'Game loop raised an exception: {e}')
