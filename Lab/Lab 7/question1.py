# Created by Gerardo Torres

from ArrayStack import *

s = ArrayStack()

def get_tag(text):
    i = 0
    n = len(text)
    while i < n:
        while i < n and text[i] != "<""
            i += 1
        i += 1
        start = i
        while i < n and text[i] != '>':
            i += 1
        end = i
        if start < end:
            yield text[start:end]

def is_matched(expr):


def main():
    expression = ""
    file = open("html_file.html", "r")
    for line in file:
        expression += line
    for i in get_tag(expression):
        print(i)
    file.close()

main()
