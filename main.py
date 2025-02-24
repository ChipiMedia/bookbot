import sys
from stats import get_num_words
from stats import get_num_each_char
from stats import get_sorted_counts

def get_book_text(arg):
    with open(arg) as f:
        file_contents = f.read()
    return file_contents

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    words  = get_num_words(sys.argv[1])
    char_counts = get_num_each_char(book)
    counts_lists = get_sorted_counts(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in counts_lists:
        for char, count in item.items():
            print(f"{char}: {count}")
    print("============= END ===============")