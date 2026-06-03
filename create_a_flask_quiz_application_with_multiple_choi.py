from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import escape

app = Flask(__name__)

# Sample questions for the quiz
questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Berlin', 'Madrid', 'Paris', 'Rome'],
        'answer': 'Paris'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
        'answer': 'Mars'
    },
    {
        'question': 'Who wrote Hamlet?',
        'options': ['Charles Dickens', 'J.K. Rowling', 'William Shakespeare', 'Leo Tolstoy'],
        'answer': 'William Shakespeare'
    }
]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for i, question in enumerate(questions):
        selected_option = request.form.get(f'question-{i}')
        if selected_option == question['answer']:
            score += 1
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)

# HOW TO RUN:
# pip install -r requirements.txt
# python create_a_flask_quiz_application_with_multiple_choi.py
# Then open: http://127.0.0.1:5000