# stats.py

def get_num_words(text):
    """Counts the number of words in the given text."""
    words = text.split()
    return len(words)

def get_char_counts(text):
    """Counts the occurrences of each character in the text."""
    char_counts = {}
    lowered_text = text.lower()
    for char in lowered_text:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_on_count(dict_item):
    """Returns the 'count' value from a dictionary item for sorting."""
    return dict_item["count"]

def sort_char_counts(char_counts_dict):
    """Converts char counts dict to a sorted list of dicts."""
    char_list = []
    for char, count in char_counts_dict.items():
        char_list.append({"char": char, "count": count})
    
    char_list.sort(reverse=True, key=sort_on_count)
    
    return char_list