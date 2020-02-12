import data_manager

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/list')
def main_page():
    return render_template('index.html', table_elements = data_manager.sort_questions())


if __name__ == '__main__':
    app.run(
        debug=True
    )