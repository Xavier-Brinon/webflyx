from typing import TypedDict

class CharacterCount(TypedDict):
    char: str
    num: int

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

def sort_on(items):
    return items["num"]

def sort_frequency(frequency: dict[str, int]) -> List[CharacterCount]:
    toListCharCount: List[CharacterCount] = []
    for freq in frequency:
        toListCharCount.append({"char": freq, "num": frequency[freq]})
    toListCharCount.sort(reverse=True, key=sort_on)
    return toListCharCount

