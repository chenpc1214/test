vowel = set("aeiou")
word = input("provide a word to search for vowels:")

i = vowel.intersection(set(word))
j = sorted(list(i))
print(j)
