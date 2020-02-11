import data_manager

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/list')
def main_page():
    return render_template('index.html', questions = data_manager.read_from_file('sample_data/question.csv'))

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )