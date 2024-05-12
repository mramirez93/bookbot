# def main():
#     with open("books/frankenstein.txt") as file:
#         content = file.read()
#         print(content)

def word_count():
    with open("books/frankenstein.txt") as file:
        content = file.read()
        word_list = str(content).split()
        total_count = len(word_list)
        print(f"{total_count} words found in the document")



def character_dictionary():
    with open("books/frankenstein.txt") as file:
        new_dict = {}     
        content = file.read()
        word_list = str(content)
    for letter in word_list:
        lowered_letter = letter.lower()
        if lowered_letter in new_dict:
            new_dict[lowered_letter] += 1
        else:
            new_dict[lowered_letter] = 1
    sorted_list = []
    for iter in new_dict:
        iterable = f"The '{iter}' character was found {new_dict[iter]} times"
        sorted_list.append(iterable)
    final_list = sorted(sorted_list)
    for item in final_list:
        print(item)




    

print("---Begin report of books/frankenstein.txt---")
# main()
word_count()
character_dictionary()
print("---End of Report---")
