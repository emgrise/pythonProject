def rev_str_only_alf(text):
    text_list = text.split(' ')

    new_list = []
    for word in text_list:
        new_word = ''
        letters = [char for char in word if char.isalpha()]
        digits = [char for char in word if char.isdigit()]
        symbols = [char for char in word if not char.isalpha() and not char.isdigit()]
        for char in word:
            if char.isalpha():
                new_word += letters.pop()
            elif char.isdigit():
                new_word += digits.pop(0)
            else:
                new_word += symbols.pop(0)
        new_list.append(new_word)

    reversed_text = ' '.join(new_list)
    return reversed_text