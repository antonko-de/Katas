def duplicate_count(text):

    formatted_text = text.lower()
    dict_chars = {}

    for chara in formatted_text:
        dict_chars[chara]=formatted_text.count(chara)

    counter = 0
    for num in dict_chars.values():
        if num > 1:
            counter += 1

    return counter



print(duplicate_count('aabBcde'))