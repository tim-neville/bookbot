import sys
from stats import count_words
from stats import count_characters
from stats import sort_chars_and_counts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def missing_sys_args(args):
    return len(args) < 2

def main():
    if (missing_sys_args):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    filepath="books/frankenstein.txt"
    print(f"Analyzing book found at {filepath}...")
    file_contents = get_book_text(filepath)

    print("----------- Word Count ----------")
    word_count = count_words(file_contents)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    character_counts_dict = count_characters(file_contents)

    sorted_list_char_counts = sort_chars_and_counts(character_counts_dict)

    for key in sorted_list_char_counts:
        if (key["char"].isalpha()):
            print(f"{key["char"]}: {key["num"]}")

    print("============= END ===============")

main()