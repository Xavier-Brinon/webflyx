def get_book_text(file_path: str) -> str:
    with open(file_path, 'r', encoding="utf-8") as f:
        file_content = f.read()
        return file_content

def main():
    book_path = "./books/frankenstein.txt"
    book = get_book_text(book_path)
    print(book)

main()
