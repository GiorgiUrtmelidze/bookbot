from stats import *
import sys

def get_book_text(filepath):
    text = ""
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    text = get_book_text(path)
    dictionary = count_characters(text)
    sorted_list = sort_dictionary(dictionary)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    print("--------- Character Count -------")

    for i in range(len(sorted_list)):
        print(f"{(sorted_list[i])['char']}: {sorted_list[i]['freq']}")

    print("============= END ===============")

main()


