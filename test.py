def rev_text(text: str) -> str:
    """ Reverse string"""
    text_list = text.split(' ')

    new_list = []
    for word in text_list:
        letters = [char for char in word if char.isalpha()]
        dig_and_syb = [char for char in word if not char.isalpha()]
        new_list.append(add_sorted(word, letters, dig_and_syb))
    text = ' '.join(new_list)
    return text


def add_sorted(word: str, letters: list, dig_and_syb: list) -> str:
    """ Adding letters,digital and symbols from lists for create new sorted word. """
    new_word = ''
    for char in word:
        if not char.isalpha():
            new_word += dig_and_syb.pop(0)
        else:
            new_word += letters.pop()
    return new_word


if __name__ == '__main__':
    cases = [
        ('ksby', 'ybsk'),
        ('a1bcd efg!h', 'd1cba hgf!e'),
        (' ', ' ')
    ]
    for text, revers_text in cases:
        assert rev_text(text=text) == revers_text
