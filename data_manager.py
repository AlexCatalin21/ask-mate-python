import csv
questions={'id': '', 'submission_time': '', 'view_number': '', 'vote_number': '', 'title': '', 'message': '', 'image': ''}
def read_from_file(filename):
    with open(filename, "r") as file:
        for row in file:
            for i in row:
                questions.update(i = 0)
    return questions


print(read_from_file("question.csv"))