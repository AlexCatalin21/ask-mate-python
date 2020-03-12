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
def write_to_answers(cursor, question_id, message,user_id=None):
    image = 'None'
    vote_number = 0
    submission_time = time.time()
    submission_time = datetime.utcfromtimestamp(submission_time).strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("""
                    INSERT INTO answer (submission_time, vote_number, question_id, message, image,user_id) VALUES (%s, %s, %s, %s, %s, %s);
                    """, (submission_time, vote_number, question_id, message, image, user_id))


@connection.connection_handler
def write_to_questions(cursor, message, title,user_id=None):
    view_number = 0
    vote_number = 0
    submission_time = time.time()
    submission_time = datetime.utcfromtimestamp(submission_time).strftime('%Y-%m-%d %H:%M:%S')
    image = 'None'
    cursor.execute("""
                        INSERT INTO question (submission_time, view_number, vote_number, title, message, image, user_id) VALUES(%s, %s, %s, %s, %s, %s, %s);
                        """, (submission_time, view_number, vote_number, title, message, image,user_id))


@connection.connection_handler
def comment_for_question(cursor, message, question_id, user_id=None):
    submission_time = time.time()
    submission_time = datetime.utcfromtimestamp(submission_time).strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("""
                        INSERT INTO comment (question_id, answer_id, message, submission_time, edited_count, user_id) VALUES(%s, NULL, %s, %s, NULL, %s);
                        """, (question_id, message, submission_time, user_id))


@connection.connection_handler
def comment_for_answer(cursor, message, answer_id, user_id=None):
    submission_time = time.time()
    submission_time = datetime.utcfromtimestamp(submission_time).strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("""
                        INSERT INTO comment (question_id, answer_id, message, submission_time, edited_count, user_id) VALUES(NULL ,%s, %s, %s, NULL, %s);
                        """, (answer_id, message, submission_time, user_id))


@connection.connection_handler
def insert_user(cursor,name,password):
    submission_time = datetime.now()
    cursor.execute("""
                        INSERT INTO users (username, password, registration_date)
                        VALUES (%s,%s,%s);
                        """,(name,password,submission_time))