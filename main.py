from stats import count_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def sort_on(items):
    return items["count"]

def main():
    print("============ BOOKBOT ============")
    filepath="books/frankenstein.txt"
    print(f"Analyzing book found at {filepath}...")
    file_contents = get_book_text(filepath)

    print("----------- Word Count ----------")
    word_count = count_words(file_contents)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    character_counts = count_characters(file_contents)

    #double dictionary char: value and count: value

    # character_counts.sort(reverse=True, key=sort_on)

    for key in character_counts:
        value = character_counts[key]
        print(f"'{key}': {value}")

    print("============= END ===============")

main()