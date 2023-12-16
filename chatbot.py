import random
import csv

def response(text):

    if text.find("Northeastern") >= 0:
        return "I noticed you mentioned Northeastern. I graduated from there in 1990!"
    if text.find("raised to") >= 0 or text.find("plus") >= 0 or text.find("minus") >= 0 or text.find("times") >= 0 or text.find("divided by") >= 0:
        return str(string_to_math(text))
    if text.find("^") >= 0 or text.find("+") >= 0 or text.find("-") >= 0 or text.find("*") >= 0 or text.find("/") >= 0:
        return str(string_to_math(text))
    
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
    file = read_csv("responses.csv")
    question = words_in_text(text[0])
    line_num = find_best_line(question, file)

    if line_num == -1:
        with open('responses.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';')
                writer.writerow(text)
    else:
        file[line_num] += text[1:]
        print(file)
        with open("responses.csv", "w") as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for l in file:
                writer.writerow(l)


    #find best line. Take the text, find the words in it. then find the best line then
    #add all responses to the end of that line. 

def pig_latin(sentence):
    sentence_list = sentence.split(" ")
    sentence_list = [pig_latin_word(word) for word in sentence_list]
    return " ".join(sentence_list)

def pig_latin_word(word):
    word = word.lower()
    vowels = ["a", "e", "i", "o", "u"]
    if word[0] in vowels:
        return word + "ay"
    else:
        return word[1:] + word[0] + "ay"

def string_to_math(str):
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
    operations = ["plus", "minus", "times", "divided by", "raised to"]
    operations2 = ["+", "-", "*", "/", "**"]
    #split all
    #then if the length is four join the middle two to get the operation
    str = str.rstrip("?.!")
    str = str.split(" ")

    str_split = []
    for i in range(len(str)):
        if str[i] == "raised" and str[i+1] == "to":
            str_split += ["raised to"]
        if str[i] in num_list or str[i] in operations:
            str_split += [str[i]]
        if str[i].isnumeric():
            str_split += [str[i]]
        if str[i] == "^":
            str_split += ["raised", "to"]
        if str[i] in operations2:
            index = operations2.index(str[i])
            str_split += [operations[index]]

    operation = ""
    num1 = 0
    num2 = 0
    if (len(str_split) == 4):
        operation = str_split[1] + " " + str_split[2]
        num1 = str_split[0]
        num2 = str_split[3]
    else:
        operation = str_split[1]
        num1 = str_split[0]
        num2 = str_split[2]
        if not num1.isnumeric():
            num1 = num_list.index(num1)
        if not num2.isnumeric():
            num2 = num_list.index(num2)
    
    num1 = int(num1)
    num2 = int(num2)

    if operation == operations[0]:
        return num1 + num2
    elif operation == operations[1]:
        return num1 - num2
    elif operation == operations[2]:
        return num1 * num2
    elif operation == operations[3]:
        if (num2 != 0):
            return num1 / num2
        else:
            return "Cannot divide by 0"
    elif operation == operations[4]:
        return num1 ** num2
    else:
        return "Operation not supported"

