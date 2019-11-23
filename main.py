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
import string
from nltk import sent_tokenize
import wget
import os
import nltk
nltk.download('punkt')
global raport


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
    if os.path.exists('6.txt') == False:
        print('The file has not been downloaded, go back to the menu and select "a"')
        return menu()

    vowels = 0
    consonants = 0
    file_to_load = open(file_location.locfile+'/6.txt', 'r')
    read_file = file_to_load.read()
    read_file.lower()

    for i in read_file:
        if(ord(i) == 65 or ord(i) == 69 or ord(i) == 73
           or ord(i) == 79 or ord(i) == 85
           or ord(i) == 97 or ord(i) == 101 or ord(i) == 105
           or ord(i) == 111 or ord(i) == 117):
            vowels = vowels + 1
        elif((ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90)):
            consonants = consonants + 1
    raport = open("raport.txt", "a+")
    raport.write('Total Number of Vowels in this String: '+str(vowels)+'\n')
    raport.write('Total Number of Consonants in this String: '+str(consonants)+'\n')
    raport.close()
    print("Total Number of Vowels in this String = ", vowels)
    print("Total Number of Consonants in this String = ", consonants)
    menu()


def words_count():
    print('Counting words in file...')
    # [Student B] Count words
    if os.path.exists('6.txt') == False:
        print('The file has not been downloaded, go back to the menu and select "a"')
        return menu()
    file_to_load = open(file_location.locfile+'/6.txt', 'r')
    num_words = 0
    with file_to_load as f:
        for line in f:
            words = line.split()
            if len(line) >= 2:    
                num_words += len(words)
    raport = open("raport.txt", "a+")
    raport.write('Number of words: '+str(num_words)+'\n')
    raport.close()
    print('Number of words in file : ', num_words)
    menu()


def pun_marks_count():
    print('Counting marks in file...')
    # [Student C] Count punctuation marks
    if os.path.exists('6.txt') == False:
        print('The file has not been downloaded, go back to the menu and select "a"')
        return menu()
    file_to_load = open(file_location.locfile+'/6.txt', 'r')
    read_file = file_to_load.read()
    my_list = []
    for c in read_file:
        if c == "?" or ".":
            my_list.append(c)
    number_of_marks = len(my_list)
    raport = open("raport.txt", "a+")
    raport.write('Number of marks: '+str(number_of_marks)+'\n')
    raport.close()
    print('Number of marks in file : ', number_of_marks)
    menu()


def sentence_count():
    print('Counting sentences in file...')
    # [Student C] Count sentences
    if os.path.exists('6.txt') == False:
        print('The file has not been downloaded, go back to the menu and select "a"')
        return menu()
    file_to_load = open(file_location.locfile+'/6.txt', 'r')
    read_file = file_to_load.read()
    number_of_sentences = len(sent_tokenize(read_file))
    raport = open("raport.txt", "a+")
    raport.write('Number of sentences: '+str(number_of_sentences)+'\n')
    raport.close()
    print('Number of sentences in file : ', number_of_sentences)
    menu()


def report_generator():
    print('Generating report...')
    # [Student A] Generate report about count of every letter in the file
    if os.path.exists('6.txt') == False:
        print('The file has not been downloaded, go back to the menu and select "a"')
        return menu()
    letter_Dictionary = dict()
    file_to_load = open(file_location.locfile + '/6.txt', 'r')
    for line_in_file in file_to_load:
        this_must_be_lower = line_in_file.lower()
        letters = list(this_must_be_lower)
        for letter in letters:
            if letter.isalpha():
                if letter in letter_Dictionary:
                    letter_Dictionary[letter] = letter_Dictionary[letter] + 1
                else:
                    letter_Dictionary[letter] = 1
    for dictionary_key in list(letter_Dictionary.keys()):
        str(print(dictionary_key, ':', letter_Dictionary[dictionary_key]))
    menu()


def save_report_to_file():
    print('Saving report to file...')
    # [Student C] Save statistics to the file
    raport = open("raport.txt", "r")
    print(raport.read())
    menu()


def quit_program():
    print()
    # [Student B] Close the application
    if os.path.exists(file_location.locfile+'/6.txt'):
        os.remove('6.txt')
        os.remove("raport.txt")
        quit()
    else:
        quit()


# Program start
main()
