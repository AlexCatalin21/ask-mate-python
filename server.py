import data_manager, sorting_functions

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/list')
def main_page():
    return render_template('index.html', table_elements = data_manager.read_from_file('sample_data/question.csv'))

@app.route('/question/<question_id>', methods=["GET"])
def show_questions(question_id):


    return render_template('question.html', question_elements= sorting_functions.title_and_message(question_id), answer_elements= sorting_functions.get_answer(question_id), question_id=question_id )

if __name__ == '__main__':
    app.run(
        debug=True
    )