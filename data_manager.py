import csv


def read_from_file(filename):
    with open(filename, "r") as file:
        elements = csv.DictReader(file)
        list_of_dict = []
        for row in elements:
            list_of_dict.append(row)
        return list_of_dict


def sort_questions():
    questions = []
    sorted_list = sorted(read_from_file(
        "sample_data/question.csv"), key=lambda k: k["submission_time"], reverse=True)
    return sorted_list


