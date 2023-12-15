import random
import csv
#modification

def response(text):

    if text.find("Northeastern") >= 0:
        return "I noticed you mentioned Northeastern. I graduated from there in 1990!"
    
    file = read_csv("responses.csv")
    text = words_in_text(text)
    line_num = find_best_line(text, file)

    if line_num == -1:
        return "I don't have the vocabulary yet to respond to that. Train me on a response!"
    
    else:
        line = file[line_num]
        return line[random.randint(1,len(line)-1)]
    
#reads the file and returns a list where each element represents a row of a line.    
def read_csv(file):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        all_lines = []
        for line in reader:
            all_lines += [line]
        return all_lines
    
#formats the string to return only the unique words
def words_in_text(text):
    text = text.split()

    #removes everything in the string unless it is an alphabetical character
    for i in range(len(text)):
        alpha_word = ""
        for char in text[i]:
            if char.isalpha():
                alpha_word += char
        alpha_word = alpha_word.lower()
        text[i] = alpha_word
    
    #removes common words
    return set(text)

#scan thru each line excluding the header
#format the string accordingly
#then keep track of the line number that had the most intersections
#takes in a formatted text input and a formatted file input
#returns the line number of the file that best matches the input text.
def find_best_line(text, file):
    line_num = -1
    max_num = 0

    for i in range(1, len(file)):
        question = file[i][0]
        question = words_in_text(question)
        num_intersect = len(text & question)

        if max_num < num_intersect:
            line_num = i
            max_num = num_intersect
    
    return line_num

#takes in an array of user text where the first thing is a question and rest are answers
def add_to_csv(text):
    with open('responses.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            print(text)
            writer.writerow(text)


