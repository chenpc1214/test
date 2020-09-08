fruits = {"watermelon":15,"banana":20,
          "pineapple":25,"orange":12,
          "apple":18}

print(fruits)

for name in sorted(fruits.keys()):
    print(name, ":" ,fruits[name])
