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
