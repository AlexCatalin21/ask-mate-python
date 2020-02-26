import connection

@connection.connection_handler
def title_and_message(cursor, id):
    cursor.execute(f"""
                    SELECT title, message FROM question
                    WHERE id = {id};
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
