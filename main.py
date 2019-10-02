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


def main():
    menu()


def menu():
    print('**********Import Menu**********')
    print()
    category = input("Chose one of the options:\n"
                     "A: Download text file from source.\n"
                     "B: Count letters in file.\n"
                     "C: Count words in file.\n"
                     "D: Count punctuation marks in file.\n"
                     "E: Count sentences.\n"
                     "F: Generate report about count of every letter in file.\n"
                     "G: Save report.\n"
                     "Q: Quit application.\n"
                     "Enter your choice: ")

    if category == "A" or category == "a":
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


def download_file():
    print()
    # [Student B] Downloading text file from the internet


def letter_count():
    print()
    # [Student A] Count letters


def words_count():
    print()
    # [Student B] Count words


def pun_marks_count():
    print()
    # [Student C] Count punctuation marks


def sentence_count():
    print()
    # [Student C] Count sentences


def report_generator():
    print()
    # [Student A] Generate report about count of every letter in the file


def save_report_to_file():
    print()
    # [Student C] Save statistics to the file


def quit_program():
    print()
    # [Student B] Close the application


# Program start
main()
