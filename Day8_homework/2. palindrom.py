from pprint import pprint
import string
import re


def is_palindrome(s):
    rev = ''.join(reversed(s))

    if (s == rev):
        return True
    return False


with open('words.txt') as f:
    lines = [line.strip() for line in f]



for word in lines:
    word = word.lower().replace(".", "").replace(",", "").replace("!", "")
    if word and is_palindrome(word):
        print(word)



