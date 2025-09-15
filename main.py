import sys
from stats import count_words
from stats import count_characters
from stats import sort_chars_and_counts

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def check_filepath(args):
    try:
        filepath=args[1]
        return filepath
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    filepath = check_filepath(sys.argv)

    print("============ BOOKBOT ============")
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