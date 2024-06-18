from collections import Counter

def word_ocurrence_map(string: str, only_top:int = None) -> list[str, int]:
    """
    Given a string, return its most common words, ordered from most to least frequent

    - String: String to be analyzed.
    - Only_top: If set, returns only the top N most frequent words.
    """

    ocurrence_counter = Counter(string.strip().split(' '))
    return ocurrence_counter.most_common(only_top)
        