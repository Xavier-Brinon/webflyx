# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

## Usage

BookBot analyzes a book's text, reporting its total word count and the
frequency of each letter. Pass the path to a book file as the only argument:

```bash
uv run main.py <path_to_book>
```

For example:

```bash
uv run main.py books/frankenstein.txt
```

Available books in `books/`:

- `books/frankenstein.txt`
- `books/mobydick.txt`
- `books/prideandprejudice.txt`

If you run it without an argument, it prints a usage message and exits:

```
Usage: python3 main.py <path_to_book>
```
