def open_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_char(text):
    char_dict = {}
    for ch in text.lower():
        if ch in char_dict:
            char_dict[ch] += 1
        else:
            char_dict[ch] = 1
    return char_dict

def print_report(book_path, w_count, char_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{w_count} words found in the document\n")
    for k, v in sorted(char_dict.items(), reverse=True, key=lambda item: item[1]):
        if k.isalpha():
            print(f"The {k} character was found {v} times")
    print("--- End report ---")

def main():
    book_path = "books/frankenstein.txt"
    book = open_book(book_path)
    num_words = count_words(book)
    char_count = count_char(book)
    print_report(book_path, num_words, char_count)

main()