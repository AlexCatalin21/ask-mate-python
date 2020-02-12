import data_manager
def title_and_message(id):
    list_of_title= []
    list_of_message = []
    final_list = []
    for dictionar in data_manager.read_from_file("sample_data/question.csv"):
        if dictionar["id"] == id:
            list_of_title.append(dictionar["title"])
            list_of_message.append(dictionar['message'])
    final_list.append(list_of_title)
    final_list.append(list_of_message)
    return final_list



def get_answer(id):
    list_of_answers =  []
    for dictionar in data_manager.read_from_file("sample_data/answer.csv"):
            if dictionar["question_id"] == id:
                list_of_answers.append(dictionar['message'])
    return list_of_answers

