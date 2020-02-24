import data_manager,csv


def sort_questions():
    sorted_list = sorted(data_manager.read_from_file("sample_data/question.csv"), key=lambda k: k["submission_time"], reverse=True)
    return sorted_list


def generate_id(filename):
    list_of_dict = data_manager.read_from_file(filename)
    list_of_id = []
    for dictionary in list_of_dict:
        list_of_id.append(int(dictionary["id"]))
    my_id = max(list_of_id)+ 1
    return my_id


def remove_question(id):
    list_of_questions = data_manager.read_from_file("sample_data/question.csv")
    for dictionar in list_of_questions:
        if dictionar["id"] == id:
            list_of_questions.remove(dictionar)
            break
    QUESTION_HEADERS = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
    with open('sample_data/question.csv','w') as file:
        writer=csv.DictWriter(file, fieldnames= QUESTION_HEADERS)
        writer.writeheader()
        for dict in list_of_questions:
            writer.writerow(dict)


def remove_answer(id):
    list_of_answers = data_manager.read_from_file("sample_data/answer.csv")
    for dictionar in list_of_answers:
        if dictionar["question_id"] == id:
            list_of_answers.remove(dictionar)
            break
    ANSWER_HEADERS = ["id","submission_time","vote_number","question_id","message","image"]
    with open('sample_data/answer.csv','w') as file:
        writer=csv.DictWriter(file, fieldnames=ANSWER_HEADERS)
        writer.writeheader()
        for dict in list_of_answers:
            writer.writerow(dict)


def question_vote(question_id, vote):
    filename = "sample_data/question.csv"
    sorted_list = sort_questions()
    for item in sorted_list:
        if str(item['id']) == str(question_id):
            update_vote = int(item['vote_number']) + vote
            item['vote_number'] = update_vote
    with open(filename, "w") as file:
        HEADERS = ["id", "submission_time", "view_number","vote_number",
                   "title", "message", "image"]
        elements = csv.DictWriter(file, fieldnames=HEADERS)
        elements.writeheader()
        for dict in sorted_list:
            elements.writerow(dict)


def answer_vote(answer_id, vote):
    filename = "sample_data/answer.csv"
    answer_list = data_manager.read_from_file(filename)
    for item in answer_list:
        if str(item['id']) == str(answer_id):
            update_vote = int(item['vote_number']) + vote
            item['vote_number'] = update_vote
    with open(filename, "w") as file:
        HEADERS = ["id", "submission_time","vote_number",
                   "question_id", "message", "image"]
        elements = csv.DictWriter(file, fieldnames=HEADERS)
        elements.writeheader()
        for dict in answer_list:
            elements.writerow(dict)


def increase_view(question_id):
    filename = "sample_data/question.csv"
    sorted_list = data_manager.read_from_file(filename)
    for item in sorted_list:
        if str(item['id']) == str(question_id):
            update_vote = int(item['view_number']) + 1
            item['view_number'] = update_vote
    with open(filename, "w") as file:
        HEADERS = ["id", "submission_time", "view_number", "vote_number",
                   "title", "message", "image"]
        elements = csv.DictWriter(file, fieldnames=HEADERS)
        elements.writeheader()
        for dict in sorted_list:
            elements.writerow(dict)