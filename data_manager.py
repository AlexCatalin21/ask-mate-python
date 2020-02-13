import csv
import time


def read_from_file(filename):
    with open(filename, "r") as file:
        elements = csv.DictReader(file)
        list_of_dict = []
        for row in elements:
            list_of_dict.append(row)
        return list_of_dict

def write_to_file(filename, question_id, message):
    with open(filename, "a+") as file:
        HEADERS = ["id", "submission_time", "vote_number", "question_id", "message", "image"]
        elements = csv.DictWriter(file, fieldnames=HEADERS)
        submission_time = int(time.time())
        vote_number = 0
        message = message
        image = ""
        new_id = generate_id()
        elements.writerow({"id": new_id,
                           "submission_time": submission_time,
                           "vote_number": vote_number,
                           "question_id" : question_id,
                           "message" : message,
                           "image": image}
                            )



def sort_questions():
    questions = []
    sorted_list = sorted(read_from_file("sample_data/question.csv"), key=lambda k: k["submission_time"], reverse=True)
    return sorted_list


def generate_id():
    list_of_dict = read_from_file("sample_data/answer.csv")
    list_of_id = []
    for dictionary in list_of_dict:
        list_of_id.append(int(dictionary["id"]))
    my_id = max(list_of_id)+ 1
    return my_id

