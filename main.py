# s3.zylowski.net/public/input/6.txt

"""
[Student A] Menu of application
[Student B] Downloading text file from the internet
[Student A] Count letters
[Student B] Count words
[Student C] Count punctuation marks
[Student C] Count sentences
[Student A] Generate report about count of every letter in the file
[Student C] Save statistics to the file
[Student B] Close the application
"""
import wget
import os
import nltk
import string
from nltk.tokenize import sent_tokenize


def main():
    menu()


def menu():
    print('**********Import Menu**********')
    print()
    category = input("Chose one of the options:\n"
                     "X: File location. \n"
                     "A: Download text file from source.\n"
                     "B: Count letters in file.\n"
                     "C: Count words in file.\n"
                     "D: Count punctuation marks in file.\n"
                     "E: Count sentences.\n"
                     "F: Generate report about count of every letter in file.\n"
                     "G: Save report.\n"
                     "Q: Quit application.\n"
                     "Enter your choice: ")
    if category == 'X' or category == 'x':
        file_location()
    elif category == "A" or category == "a":
        download_file()
    elif category == "B" or category == "b":
        letter_count()
    elif category == "C" or category == "c":
        words_count()
    elif category == "D" or category == "d":
        pun_marks_count()
    elif category == "E" or category == "e":
        sentence_count()
    elif category == "F" or category == "f":
        report_generator()
    elif category == "G" or category == "g":
        save_report_to_file()
    elif category == "Q" or category == "q":
        quit_program()
    else:
        print("Choice not on the list.\n Try again.")
        menu()


def file_location():
    file_location.locfile = input('Enter file destination: ')
    menu()


def download_file():
    print('Downloading file to the directory...')
    # [Student B] Downloading text file from the internet
    directo = file_location.locfile
    url = 'https://s3.zylowski.net/public/input/6.txt'
    wget.download(url, directo)
    print('File downloaded to the directroy ' + directo)
    menu()


def letter_count():
    print('Counting letters in file...')
    # [Student A] Count letters
    sum_letter = 0
    file_to_load = open(file_location.locfile, 'r')
    read_file = file_to_load.read()
    for letter in range(len(read_file)):
        if read_file[letter].isalpha():
            sum_letter += 1

    print('Number of letters in file : ', sum_letter)


def words_count():
    print()
    # [Student B] Count words


def pun_marks_count():
    print('Counting marks in file...')
    # [Student C] Count punctuation marks
    if not os.path.isfile(file_location.locfile):
        print('The file has not been downloaded, go back to the menu and select "a"')
        return menu()
    file_to_load = open(file_location.locfile, 'r')
    read_file = file_to_load.read()
    my_list = []
    for c in read_file:
        if c in string.punctuation:
            my_list.append(c)
    number_of_marks = len(my_list)
    print('Number of marks in file : ', number_of_marks)
    menu()


def sentence_count():
    print('Counting sentences in file...')
    # [Student C] Count sentences
    if not os.path.isfile(file_location.locfile):
        print('The file has not been downloaded, go back to the menu and select "a"')
        return menu()
    file_to_load = open(file_location.locfile, 'r')
    read_file = file_to_load.read()
    number_of_sentences = len(sent_tokenize(read_file))
    print('Number of sentences in file : ', number_of_sentences)
    menu()


def report_generator():
    print()
    # [Student A] Generate report about count of every letter in the file


def save_report_to_file():
    print()
    # [Student C] Save statistics to the file


def quit_program():
    print()
    # [Student B] Close the application
    if os.path.exists(file_location.locfile+'6.txt'):
        os.remove(file_location.locfile+'6.txt')
        quit()
    else:
        quit()

# Program start
main()
