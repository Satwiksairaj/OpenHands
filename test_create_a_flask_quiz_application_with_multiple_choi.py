import pytest
from flask import Flask
from create_a_flask_quiz_application_with_multiple_choi import app

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'What is the capital of France?' in response.data

@pytest.mark.parametrize('question_index, selected_option, expected_score', [
    (0, 'Paris', 1),
    (1, 'Mars', 2),
    (2, 'William Shakespeare', 3)
])
def test_submit(client, question_index, selected_option, expected_score):
    data = {f'question-{question_index}': selected_option}
    response = client.post('/submit', data=data)
    assert response.status_code == 200
    assert f'Your score is: {expected_score}' in response.data