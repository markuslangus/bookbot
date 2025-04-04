# main.py

from stats import get_num_words, get_char_counts, sort_char_counts
import sys

def get_book_text(path):
    """Reads the content of a file at the given path and returns it as a string."""
    with open(path) as f:
        return f.read()

def main():
    """Main function to execute the book reading, analysis, and report generation."""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = f"{sys.argv[1]}"
    
    file_contents = get_book_text(book_path)
    
    num_words = get_num_words(file_contents)
    
    char_dict = get_char_counts(file_contents)
    
    sorted_char_list = sort_char_counts(char_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for item in sorted_char_list:
        char = item["char"]
        count = item["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


main()