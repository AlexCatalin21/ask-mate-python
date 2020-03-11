import data_manager, sorting_functions, util

from flask import Flask, render_template, request, redirect, url_for, session, escape, flash

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=["GET", "POST"])
@app.route('/list', methods=["GET", "POST"])
@app.route('/search')
def main_page():
    if 'username' in session:
        if request.method == 'POST':
            order = request.form['order']
            return render_template('index.html', table_elements=util.sort_questions(order), username = session['username'])
        if request.args:
            search_phrase=request.args.get('phrase')
            util.search_a_phrase(search_phrase)
            return render_template('index.html', table_elements=util.search_a_phrase(search_phrase), search_phrase=search_phrase, username = session['username'])
        return render_template('index.html', table_elements=util.sort_questions(), username = session['username'])
    return render_template('index.html', table_elements=util.sort_questions())

@app.route('/question/<question_id>', methods=["GET"])
def show_questions(question_id):
    util.increase_view(question_id)
    return render_template('question.html', question_elements = sorting_functions.title_and_message(question_id), answer_elements= data_manager.read_from_table('answer'), question_id=question_id,  comments = data_manager.read_from_table('comment'))


@app.route('/question/<question_id>/new-answer', methods=["GET", "POST"])
def new_answers(question_id):
    if request.method == 'POST':
        message = request.form['message']
        data_manager.write_to_answers(question_id, message)
        return redirect(url_for('show_questions', question_id=question_id))
    return render_template('new_answer.html', question_id=question_id)

@app.route("/question/<question_id>/delete", methods=["GET", "POST"])
def remove_a_question(question_id):
    if request.method == 'GET':
        for dictionar in util.get_question_id_from_ans(question_id):
            answer_id=dictionar['id']
            util.remove_comment_of_answer(answer_id)
        util.remove_comment_of_question(question_id)
        util.remove_answer(question_id)
        util.remove_question(question_id)
    return redirect(url_for('main_page'))


@app.route('/add_question', methods=["GET", "POST"])
def add_question():
    if request.method == 'POST':
        message = request.form['message']
        title = request.form['title']
        data_manager.write_to_questions(message, title)
        question_id = data_manager.generate_id()
        return redirect(url_for('show_questions', question_id = question_id))
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
def answer_vote_down(answer_id, question_id):
    util.answer_vote(answer_id, -1)
    return redirect(url_for('show_questions', question_id=question_id))

@app.route('/answer/<answer_id>/edit', methods=['GET',"POST"])
def edit_answer(answer_id):
    if request.method == 'POST':
        message = request.form['message']
        util.edit_an_answer(message, answer_id)
        return redirect(url_for('show_questions', question_id=util.get_question_id(answer_id)))
    return render_template("edit_answer.html",answer_id=answer_id,answers= data_manager.read_from_table('answer'))


@app.route('/comment/<comment_id>/edit', methods=["GET", "POST"])
def edit_comment(comment_id):
    if request.method == 'POST':
        message = str(request.form['message'])
        util.edit_comment(message, comment_id)
        answer_id = util.get_answer_id_by_com(comment_id)
        if answer_id == None:
            question_id = util.get_question_id_by_comm(comment_id)
        else:
            question_id = util.get_question_id(answer_id)
        return redirect(url_for('show_questions', question_id=question_id))
    return render_template("edit-comments.html", comment_id=comment_id, comments= data_manager.read_from_table('comment'))


@app.route('/question/<question_id>/new-comment', methods=['GET', 'POST'])
def add_comment_to_question(question_id):
    if request.method == 'POST':
       message = request.form['message']
       data_manager.comment_for_question(message, question_id)
       return redirect(url_for('show_questions', question_id=question_id))
    return render_template("comment_for_question.html", question_id=question_id)


@app.route('/answer/<answer_id>/new-comment', methods=['GET', 'POST'])
def add_comment_to_answer(answer_id):
    if request.method == 'POST':
       message = request.form['message']
       data_manager.comment_for_answer(message, answer_id)
       return redirect(url_for('show_questions', question_id=util.get_question_id(answer_id)))
    return render_template("comment_for_answer.html", answer_id=answer_id)


@app.route("/comments/<comment_id>/delete")
def remove_a_comment(comment_id):
    if request.method == 'GET':
        answer_id = util.get_answer_id_by_com(comment_id)
        if answer_id == None:
            question_id = util.get_question_id_by_comm(comment_id)
        else:
            question_id = util.get_question_id(answer_id)
        util.remove_coment(comment_id)
    return redirect(url_for('show_questions', question_id=question_id))

@app.route('/registration',methods=['GET','POST'])
def registration():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['psw']
        password = util.hash_password(password)
        data_manager.insert_user(name,password)
        return redirect(url_for('main_page'))
    return render_template('registration.html')

@app.route('/users_list')
def show_users():
    return render_template('users_list.html',table_elements=data_manager.read_from_table('users'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if util.confirm_user(request.form['uname']):
            session['username'] = request.form['uname']
            session['password'] = request.form['psw']
            passs = util.check_credentials(session['username'])['password']
            if util.verify_password(session['password'], passs):
                return redirect(url_for('main_page'))
        return redirect(url_for('main_page'))


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('main_page'))

if __name__ == '__main__':
    app.run(
        debug=True
    )