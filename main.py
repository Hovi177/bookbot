from stats import count_words
from stats import char_count
import sys

def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        count = count_words(path)
        letter_count = char_count(path)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {count} total words")
        print("--------- Character Count -------")
        for item in letter_count:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()