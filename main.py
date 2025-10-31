from stats import *
import sys

def report(filepath: str):
    print("=============== BOOKBOT ===============")
    print(f"Analyzing book found at {filepath}...")
    print("-------------- Word Count -------------")
    text = get_book_text(filepath)
    print(f"Found {count_words(text)} total words")
    print("------------ Character Count ----------")
    character_count = count_characters(text)
    sorted_character_count = sort_character_count(character_count)

    for item in sorted_character_count:
        print(f"{item["char"]}: {item["num"]}")
    
    print("================= END =================")
    


def main():
    if len(sys.argv) <= 1:
        print("error: no filepath specified")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    for arg in sys.argv[1:]:
        report(arg)
        print()


main()