import data_manager, sorting_functions, util

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/list')
def main_page():
    return render_template('index.html', table_elements = util.sort_questions())

@app.route('/question/<question_id>', methods=["GET"])
def show_questions(question_id):
    util.increase_view(question_id)
    return render_template('question.html', question_elements= sorting_functions.title_and_message(question_id), answer_elements= data_manager.read_from_file("sample_data/answer.csv"), question_id=question_id )


@app.route('/question/<question_id>/new-answer', methods=["GET", "POST"])
def new_answers(question_id):
    if request.method == 'POST':
        message = request.form['message']
        data_manager.write_to_answers("sample_data/answer.csv", question_id, message)
        return redirect(url_for('show_questions', question_id=question_id))
    return render_template('new_answer.html', question_id=question_id)

@app.route("/question/<question_id>/delete", methods=["GET", "POST","DELETE"])
def remove_a_question(question_id):
    if request.method == 'GET':
        util.remove_question(question_id)
        util.remove_answer(question_id)
    return redirect(url_for('main_page'))


@app.route('/add_question', methods=["GET", "POST"])
def add_question():
    if request.method == 'POST':
        message = request.form['message']
        title = request.form['title']
        question_id = util.generate_id('sample_data/question.csv')
        data_manager.write_to_questions("sample_data/question.csv", message, title)
        return redirect(url_for('show_questions', question_id=question_id))
    return render_template('add-question.html')


@app.route('/question/<question_id>/vote-up', methods=["GET"])
def question_vote_up(question_id):
    util.question_vote(question_id, 1)
    return redirect(url_for('main_page'))


@app.route('/question/<question_id>/vote-down', methods=["GET"])
def question_vote_down(question_id):
    util.question_vote(question_id, -1)
    return redirect(url_for('main_page'))

@app.route('/answer/<answer_id>/<question_id>/vote_up', methods=['GET'])
def answer_vote_up(answer_id, question_id):
    util.answer_vote(answer_id, 1)
    return redirect(url_for('show_questions', question_id=question_id))

@app.route('/answer/<answer_id>/<question_id>/vote_down', methods=['GET'])
def answer_vote_down(answer_id,question_id):
    util.answer_vote(answer_id, -1)
    return redirect(url_for('show_questions', question_id=question_id))


if __name__ == '__main__':
    app.run(
        debug=True
    )