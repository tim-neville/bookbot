def count_words(input_text):
    words = input_text.split()
    return len(words)

def count_characters(input_text):
    lower_case_words = input_text.lower()

    character_counts = {}
    for char in lower_case_words:
        if (char in character_counts):
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    return character_counts
    