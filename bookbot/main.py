from stats import nbr_words, char_frequency, sort_frequency

def get_book_text(file_path: str) -> str:
    with open(file_path, 'r', encoding="utf-8") as f:
        file_content = f.read()
        return file_content

# ============ BOOKBOT ============
# Analyzing book found at books/frankenstein.txt...
# ----------- Word Count ----------
# Found 75767 total words
# --------- Character Count -------
def print_header(book_path: str, words: int, frequency: dict[str, int]) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

def print_frequency(frequency: dict[str, int]) -> None:
    for k in frequency:
        if k['char'].isalpha():
            print(f"{k['char']}: {k['num']}")

def main():
    book_path: str = "./books/frankenstein.txt"
    book: str = get_book_text(book_path)
    words: int = nbr_words(book)
    frequency = char_frequency(book)
    print_header(book_path, words, frequency)
    sorted_frequency = sort_frequency(frequency)
    print_frequency(sorted_frequency)

main()
