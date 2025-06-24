def count_words(text):
    return len(text.split())

def count_characters(text):
    characters = {}

    for i in range(len(text)):
        if not text[i].isalpha():
            continue

        char = text[i].lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters

def sort_on(dict):
    return dict["freq"]

def sort_dictionary(dictionary):
    list_of_dictionaries = []

    for key, value in dictionary.items():
        list_of_dictionaries.append({"char" : key , "freq" : value})

    list_of_dictionaries.sort(reverse=True, key=sort_on)

    return list_of_dictionaries