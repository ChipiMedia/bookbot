def get_num_words(file):
    with open(file) as f:
        file_contents = f.read()
    file_contents_split = file_contents.split()
    count = 0
    for word in file_contents_split:
        count += 1
    num_words = count
    return f"{num_words}"

def get_num_each_char(string):
    counts = {}
    for char in string.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def get_sorted_counts(char_counts):
    """
    Takes a dictionary of character counts,
    filters only alphabetic characters,
    and returns a sorted list of single-key dictionaries.
    """
    list_of_dicts = []

    # Transform the dictionary to a list of single-key dictionaries
    for char, count in char_counts.items():
        if char.isalpha():  # Filter out non-alphabetic characters
            list_of_dicts.append({char: count})

    # Sort the list in descending order of counts
    def sort_on(dict_item):
        return list(dict_item.values())[0]

    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
    