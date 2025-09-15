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
    
def sort_on(items):
    return items["num"]

def sort_chars_and_counts(character_counts_dict):
    chars_counts_list = []
    #double dictionary char: character_counts [key] and count: character_counts [value]

    # character_counts.sort(reverse=True, key=sort_on)

    for key in character_counts_dict:
        value = character_counts_dict[key]
        chars_counts_list.append({"char":key, "num":value})

    chars_counts_list.sort(reverse=True, key=sort_on)

    return chars_counts_list
