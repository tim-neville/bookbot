from stats import count_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    word_count = count_words(file_contents)
    print(f"{word_count} words found in the document")
    
    character_counts = count_characters(file_contents)

    for key in character_counts:
        value = character_counts[key]
        print(f"'{key}': {value}")

main()