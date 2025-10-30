def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def count_words(text):
    return len(text.split())


def main():
    text = get_book_text("books/frankenstein.txt")
    print(f"Found {count_words(text)} total words")


main()