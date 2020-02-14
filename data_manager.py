import csv
import time


def read_from_file(filename):
    with open(filename, "r") as file:
        elements = csv.DictReader(file)
        list_of_dict = []
        for row in elements:
            list_of_dict.append(row)
        return list_of_dict

def write_to_answers(filename, question_id, message):
    HEADERS = []
    for dictionary in read_from_file(filename):
        for sub_dict in dictionary:
            HEADERS.append(sub_dict)
        break
    with open(filename, "a+") as file:
        elements = csv.DictWriter(file, fieldnames=HEADERS)
        submission_time = int(time.time())
        vote_number = 0
        message = message
        image = ""
        new_id = generate_id(filename)
        elements.writerow({"id": new_id,
                            "submission_time": submission_time,
                            "vote_number": vote_number,
                            "question_id" : question_id,
                            "message" : message,
                            "image": image}
                            )



def write_to_questions(filename,message,title):
    HEADERS = []
    for dictionary in read_from_file(filename):
        for sub_dict in dictionary:
            HEADERS.append(sub_dict)
        break
    with open(filename, "a+") as file:
        elements = csv.DictWriter(file, fieldnames=HEADERS)
        submission_time = int(time.time())
        vote_number = 0
        message = message
        title=title
        image = ""
        view_number = 0
        new_id = generate_id(filename)
        elements.writerow({"id": new_id,
                        "submission_time": submission_time,
                        "view_number": view_number,
                        "vote_number": vote_number,
                        "title": title,
                        "message" : message,
                        "image": image}
                            )
def sort_questions():
    sorted_list = sorted(read_from_file("sample_data/question.csv"), key=lambda k: k["submission_time"], reverse=True)
    return sorted_list


def generate_id(filename):
    list_of_dict = read_from_file(filename)
    list_of_id = []
    for dictionary in list_of_dict:
        list_of_id.append(int(dictionary["id"]))
    my_id = max(list_of_id)+ 1
    return my_id


def remove_question(id):
    list_of_questions = read_from_file("sample_data/question.csv")
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
    list_of_answers = read_from_file("sample_data/answer.csv")
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
    answer_list = read_from_file(filename)
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

