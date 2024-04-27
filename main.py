def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters_dict = get_num_letters(text)
    list_chars = set_lists_chars(num_letters_dict)
    list_chars.sort(reverse=True, key=sort_on)
    # print(f"{num_words} words found in the document")
    # print(num_letters_dict)
    print_result(book_path, num_words, list_chars)

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    letter_dict = {}
    for letter in text:
        letter_lower = letter.lower()
        if letter_lower not in letter_dict:
            letter_dict[letter_lower] = 1
        else:
            letter_dict[letter_lower] += 1
    return letter_dict

def set_lists_chars(num_letters_dict):
    new_dict_list = []
    for letter in num_letters_dict:
        temp_dict = {}
        if letter.isalpha() == True:
            temp_dict['letter'] = letter
            temp_dict['num'] = num_letters_dict[letter]
            new_dict_list.append(temp_dict)
    return new_dict_list

def sort_on(dict):
    return dict["num"]

def print_result(book_path, num_words, list_chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for char in list_chars:
        letter = char.get("letter")
        number = char.get("num")
        print(f"The '{letter}' character was found {number} times")
        pass
    print("--- End report ---")
    pass

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
