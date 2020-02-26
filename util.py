import data_manager, connection

@connection.connection_handler
def sort_questions(cursor):
    cursor.execute("""
                    SELECT * FROM question
                    ORDER BY submission_time DESC 
                    LIMIT 5; 
                    """)
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
