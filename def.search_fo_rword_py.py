def searchvowel(words):
    """display any vowels found in an  ask-for words."""
    vowel = set("aeeeiou")
    python = vowel.intersection(set(words))
    for vowel in python:
        print(python)
