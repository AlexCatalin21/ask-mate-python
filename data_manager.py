import csv

def read_from_file(filename):
    questions=[]
    with open(filename,"r") as file:
        for row in file:
            questions.append(row.strip("\n").split(','))
    return questions


print(read_from_file("sample_data/question.csv"))