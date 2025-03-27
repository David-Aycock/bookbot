#!/bin/bash

from stats import get_num_words, get_num_chars, sorted_list
import sys

def main():
    if (len(sys.argv)) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    with open(path) as f:
        contents = f.read()
    num_words = get_num_words(contents)
    print(f"{num_words} words found in the document")

    num_chars = get_num_chars(contents)
    print(num_chars)

    chars_list = sorted_list(num_chars)

    print(f""""
    ============ BOOKBOT ============
    Analyzing book found at {path}...
    ----------- Word Count ----------
    Found {num_words} total words
    --------- Character Count -------
    """)
    for character in chars_list:
        print(f"{character['char']}: {character['count']}")
    print("============= END ===============")



main()