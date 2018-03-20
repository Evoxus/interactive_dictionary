import json
import difflib
from difflib import get_close_matches

still_searching = True

data = json.load(open(r"c:\Users\mp_pr\OneDrive\Desktop\Coding\Python\python_megacourse\data.json", "r"))

def get_definition(word):
    return ' '.join(data[word])

word = ''
yeses = ('y', 'yes', 'yeah')

def user_input():
    global word
    while True:
        try:
            word = input('Enter a word you\'d like the definition for: ').lower()
            try:
                if word == get_close_matches(word, data.keys(), n=1)[0]:
                    break
                elif get_close_matches(word, data.keys(), n=1)[0] != word:
                    check = input("Did you mean {0}? (Y/N) ".format(' '.join(get_close_matches(word, data.keys(), n=1))))
                    if check in yeses:
                        word = get_close_matches(word, data.keys(), n=1)[0]
                        break
                else:
                    print("I didn't find that word.")
            except IndexError:
                print("I can't find any close matches for {0}, I don't believe it is a real word.".format(word))
            else:
                print("I didn't find that word.")
        except TypeError:
            print('Please enter a word.')

def continue_looking():
    global still_searching
    usr_input2 = input('Would you like to look for another word? (Y/N) ').lower()
    if usr_input2 in yeses:
        still_searching = True
    else:
        still_searching = False

while still_searching:
    user_input()
    print(get_definition(word))
    continue_looking()