def search_4_letters(phrase:str, letter:str="aeiou") -> set:
    """return a set of the "letters" found in phrase"""
    return set(letter).intersection(set(phrase))

