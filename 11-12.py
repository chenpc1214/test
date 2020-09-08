def ispalindromes(n):
    if n[0:] == n[::-1]:
        print("it is palindrome.")
    else:
        print("it is not palindrome.")

value = str(input("請輸入字串:"))

ispalindromes(value)
