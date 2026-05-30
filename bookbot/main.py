from stats import nbr_words, char_frequency, chars_dict_to_sorted_list
import sys

def get_book_text(file_path: str) -> str:
    with open(file_path, 'r', encoding="utf-8") as f:
        file_content = f.read()
        return file_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path: str = sys.argv[1]
    book: str = get_book_text(book_path)
    words: int = nbr_words(book)
    print(f"Found {words} total words")
    frequency = char_frequency(book)
    sorted_list = chars_dict_to_sorted_list(frequency)
    for char_count in sorted_list:
        print(char_count)

main()
