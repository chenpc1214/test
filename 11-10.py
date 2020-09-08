def ispalindrome(n):
    if n[0:] == n[::-1]:
        print("it is palindrome.")
    else:
        print("it is not palindrome.")

value = input("請輸入數值:")

ispalindrome(value)
