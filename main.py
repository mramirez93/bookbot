def main():
    path_to_file = "books/frankenstein.txt"
    book = text(path_to_file)
    total_count = word_count(book)
    character_dict = get_character_dict(book)
    chars_sorted_list = dict_to_list(character_dict)

    print(f"--Begin report of {path_to_file} ---")
    print(f"{total_count} words found in the document")
    print()

    for char in chars_sorted_list:
        if not char['char'].isalpha():
            continue
        print(f"The '{char['char']}' character was found {char['num']} times")

    print("---End report---")


def word_count(path_to_file):
    count = path_to_file.split()
    return len(count)

def sort_on(d):
    return d["num"]

def dict_to_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_character_dict(book):
    characters = {}
    for letter in book:
        lower_case = letter.lower()
        if lower_case in characters:
            characters[lower_case] += 1
        else:
            characters[lower_case] = 1
    return characters

def text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main()
