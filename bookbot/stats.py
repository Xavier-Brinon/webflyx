def sort_on(word_count: tuple[str, int]) -> int:
    return word_count[1]

def chars_dict_to_sorted_list(frequency: dict[str, int]) -> list[tuple[str, int]]:
    char_counts: list[tuple[str, int]] = []
    for char in frequency:
        char_counts.append((char, frequency[char]))
    return sorted(char_counts, reverse=True, key=sort_on)

def nbr_words(text: str) -> int:
    return len(text.split())

def char_frequency(text: str) -> dict[str, int]:
    frequency: dict[str, int] = {}
    for char in text:
        lower = char.lower()
        if lower not in frequency:
            frequency[lower] = 1
        else:
            frequency[lower] += 1
    return frequency
