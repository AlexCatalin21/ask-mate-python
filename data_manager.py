import csv


def read_from_file(filename):
    with open(filename,"r") as file:
        elements = csv.DictReader(file)
        list_of_dict=[]
        for row in elements:
            list_of_dict.append(row)
        return list_of_dict