def check_character(sentence,character):
    if not isinstance(sentence, str) and not character.isalpha():
        return "invalid data"
    counter=0
    for ch in sentence:
        if ch==character:
            counter+=1
    return counter


print(check_character('Order of the Phoenix', 'e'))
