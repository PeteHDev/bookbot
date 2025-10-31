def get_book_text(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def count_words(text: str):
    return len(text.split())

def count_characters(text: str):
    lower_case = text.lower()
    count_dict = {}

    for c in lower_case:
        if not c.isalpha(): continue

        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1

    return count_dict

def sort_character_count(character_count: dict):
    character_count_list = []
    for key in character_count:
        character_count_list.append({"char": key, "num": character_count[key]})
    
    character_count_list.sort(reverse=True, key=lambda items: items["num"])

    return character_count_list
