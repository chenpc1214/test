def searchvowel():
    """display any vowels found in an  ask-for words."""
    vowel = set("aeeeiou")
    words = input("provided a words name:")
    python = vowel.intersection(set(words))
    for vowel in python:
        print(list(vowel))
        
