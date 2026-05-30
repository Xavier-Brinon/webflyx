from stats import nbr_words

def get_book_text(file_path: str) -> str:
    with open(file_path, 'r', encoding="utf-8") as f:
        file_content = f.read()
        return file_content

def main():
    book_path: str = "./books/frankenstein.txt"
    book: str = get_book_text(book_path)
    words: int = nbr_words(book)
    message: str = f"Found {words} total words"
    print(message)

main()
