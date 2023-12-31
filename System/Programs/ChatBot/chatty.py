import random
import Data

message_data = Data.ChatData

def determine_grades(chat_and_response, inputed_data):
    lowercase_string = inputed_data.lower()
    split_sentance_list = lowercase_string.split()
    grade_linear = 0
    grade_precentage = 0

    for possible_inputs in chat_and_response[0]:
        for words in split_sentance_list:
            if words == possible_inputs:
                grade_linear+=1
    
    grade_precentage = (grade_linear/len(chat_and_response[0]))*100
    return grade_precentage

def Ask_Bot(inputed_data):
    grades = []
    for chat_and_response in message_data:
        grades.append(determine_grades(chat_and_response, inputed_data))
    
    highest_grade = max(grades)
    index = grades.index(highest_grade)
    selected_type = message_data[index]
    if not highest_grade == 0:
        return selected_type[random.randint(1,len(selected_type) - 1)]
    else:
        return random.choice(Data.Bots_unknown_responses)