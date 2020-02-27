import data_manager, connection

@connection.connection_handler
def sort_questions(cursor, header='submission_time'):
    cursor.execute(f""" SELECT * FROM question
                    ORDER BY {header} DESC 
                     LIMIT 5; """)
    sorted_list = cursor.fetchall()
    return sorted_list

@connection.connection_handler
def remove_question(cursor,id):
    cursor.execute(f"""
                    DELETE FROM question
                    WHERE id = {id}; 
                    """)


@connection.connection_handler
def remove_answer(cursor,id):
    cursor.execute(f"""
                        DELETE FROM answer
                        WHERE question_id = {id}; 
                        """)

@connection.connection_handler
def question_vote(cursor,question_id, vote):
    cursor.execute(f"""
                            UPDATE question
                            SET vote_number = vote_number+{vote}
                            WHERE id = {question_id}; 
                            """)


@connection.connection_handler
def answer_vote(cursor,answer_id, vote):
    cursor.execute(f"""
                        UPDATE answer
                        SET vote_number = vote_number+{vote}
                        WHERE id = {answer_id}; 
                    """)


@connection.connection_handler
def increase_view(cursor, question_id):
    cursor.execute(f"""
                    UPDATE question
                    SET view_number = view_number+ 1
                    WHERE id = {question_id};
                    """)



@connection.connection_handler
def edit_an_answer(cursor ,message, answer_id):
    cursor.execute("""
                    UPDATE answer
                    SET message = %s
                    WHERE id = %s;
                    """,(message,answer_id))

@connection.connection_handler
def get_question_id(cursor,answer_id):
    cursor.execute(f"""
                        SELECT question_id FROM answer
                        WHERE id = {answer_id};
                    """)
    question_id = cursor.fetchone()
    return  question_id['question_id']

@connection.connection_handler
def remove_coment(cursor, comment_id):
    cursor.execute(f"""
                    DELETE FROM comment
                    WHERE id = {comment_id};
                    """)

@connection.connection_handler
def get_question_id_by_comm(cursor, comment_id):
    cursor.execute(f"""
                    SELECT question_id FROM comment
                    WHERE id={comment_id};
                    """)
    question_id = cursor.fetchone()
    return question_id['question_id']

@connection.connection_handler
def get_answer_id_by_com(cursor, comment_id):
    cursor.execute(f"""
                    SELECT answer_id FROM comment
                    WHERE id ={comment_id};
                    """)
    answer_id = cursor.fetchone()
    return answer_id['answer_id']

@connection.connection_handler
def search_a_phrase(cursor,phrase):
    cursor.execute(f"""SELECT * FROM question
                        WHERE message LIKE '%{phrase}%' OR title LIKE '%{phrase}%';""")
    result=cursor.fetchall()
    return result
