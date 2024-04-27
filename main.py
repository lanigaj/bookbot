def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters_dict = get_num_letters(text)
    print(f"{num_words} words found in the document")
    print(num_letters_dict)

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

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
