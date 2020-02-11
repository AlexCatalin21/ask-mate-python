import csv

def read_from_file(filename):
    questions=[]
    with open(filename) as file:
        for row in csv.DictReader(open(filename)):
            newdict={}
            for key in row:
                newdict[key] = row[key].replace("\n", "<br />")
            questions.append(newdict)
    return(questions)

print(read_from_file("sample_data/question.csv"))





