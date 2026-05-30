from stats import nbr_words, char_frequency, chars_dict_to_sorted_list

def get_book_text(file_path: str) -> str:
    with open(file_path, 'r', encoding="utf-8") as f:
        file_content = f.read()
        return file_content

def main():
    book_path: str = "./books/frankenstein.txt"
    book: str = get_book_text(book_path)
    words: int = nbr_words(book)
    print(f"Found {words} total words")
    frequency = char_frequency(book)
    sorted_list = chars_dict_to_sorted_list(frequency)
    for char_count in sorted_list:
        print(char_count)

main()
