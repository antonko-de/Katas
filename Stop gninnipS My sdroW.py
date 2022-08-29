def spin_words(sentence):

    list_words = sentence.split(" ")

    list_reversed = [word[::-1] if len(word) >= 5 else word for word in list_words]
    result = ' '.join(list_reversed)
    
    return result

print(spin_words("This sentence is a sentence"))