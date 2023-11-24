def count_words(string):
    return len(string.split())

def count_characters(string):
    counts = {}
    for char in string:
        if char.isalpha():
            case_insensitive_char = char.lower()
            if case_insensitive_char in counts:
                counts[case_insensitive_char] += 1
            else:
                counts[case_insensitive_char] = 1
    return counts

with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    char_counts = count_characters(file_contents)
    keys = sorted(char_counts.keys())
    for key in keys:
        print(f"The '{key}' character was found {char_counts[key]} times")
    
    
