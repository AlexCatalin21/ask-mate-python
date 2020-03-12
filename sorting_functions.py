import connection

@connection.connection_handler
def title_and_message(cursor, id):
    cursor.execute(f"""
                    SELECT  question.id, question.submission_time, question.view_number, question.vote_number,question.title, question.message, question.image, user_id, users.username FROM question 
                        LEFT JOIN users ON (user_id=users.id)
                    WHERE question.id = {id};
                    """)
    final_list = cursor.fetchall()
    return final_list


@connection.connection_handler
def get_answer(cursor, id):
    cursor.execute(f"""
                    SELECT message FROM answer
                    WHERE question_id ={id};
                    """)
    list_of_answers = cursor.fetchall()
    return list_of_answers
