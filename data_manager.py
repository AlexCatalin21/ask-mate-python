import time
from datetime import datetime

import connection

@connection.connection_handler
def generate_id(cursor):
    cursor.execute("""SELECT MAX(id) FROM question
    """)
    id = cursor.fetchall()
    return id[0]['max']

@connection.connection_handler
def read_from_table(cursor, table):
    cursor.execute(f"""SELECT * FROM {table};""")
    name = cursor.fetchall()
    return name


@connection.connection_handler
def write_to_answers(cursor, question_id, message):
    image = 'nothing'
    vote_number = 0
    submission_time = time.time()
    submission_time = datetime.utcfromtimestamp(submission_time).strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("""
                    INSERT INTO answer (submission_time, vote_number, question_id, message, image) VALUES (%s, %s, %s, %s, %s);
                    """, (submission_time, vote_number, question_id, message, image))


@connection.connection_handler
def write_to_questions(cursor, message, title):
    view_number = 0
    vote_number = 0
    submission_time = time.time()
    submission_time = datetime.utcfromtimestamp(submission_time).strftime('%Y-%m-%d %H:%M:%S')
    image = 'nothing'
    cursor.execute("""
                        INSERT INTO question (submission_time, view_number, vote_number, title, message, image) VALUES(%s, %s, %s, %s, %s, %s);
                        """, (submission_time, view_number, vote_number, title, message, image))


@connection.connection_handler
def comment_for_question(cursor, message, question_id):
    submission_time = time.time()
    submission_time = datetime.utcfromtimestamp(submission_time).strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("""
                        INSERT INTO comment (question_id, answer_id, message, submission_time, edited_count) VALUES(%s, NULL, %s, %s, NULL);
                        """, (question_id, message, submission_time))


@connection.connection_handler
def comment_for_answer(cursor, message, answer_id):
    submission_time = time.time()
    submission_time = datetime.utcfromtimestamp(submission_time).strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("""
                        INSERT INTO comment (question_id, answer_id, message, submission_time, edited_count) VALUES(NULL ,%s, %s, %s, NULL);
                        """, (answer_id, message, submission_time))
