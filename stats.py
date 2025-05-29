def count_words(path):
    count = 0
    contents = get_book_text(path)
    words = contents.split()
    for word in words:
        count += 1
    return count

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def sortnum(letter_count):
    new_list = []
    new_dict = {}
    for key, value in letter_count.items():
        if key.isalpha():
            new_dict = {"char":key,"num":value}
            new_list.append(new_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(dict):
    return dict["num"]

def char_count(path):
    letter_count = {}
    contents = get_book_text(path)
    words = contents.split()
    for word in words:
        letter = "".join(word)
        words_uniform = letter.lower()
        for letters in words_uniform:
            if letters in letter_count:
                letter_count[letters] += 1
            else:
                letter_count[letters] = 1
    new_list = sortnum(letter_count)
    return new_list