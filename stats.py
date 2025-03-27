def get_num_words(contents):
    
    words = contents.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def get_num_chars(contents):
    char_count = {}

    for char in contents:
        char = char.lower()

        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sorted_list(char_count):
    chars_list = []

    for char, count in char_count.items():
        char_dict = {"char": char, "count": count}

        chars_list.append(char_dict)
    chars_list.sort(reverse=True, key=sort_on)

    for char in chars_list:
        print(char)

    return chars_list

def sort_on(dict):
    return dict["count"]