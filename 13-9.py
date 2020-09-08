import keyword



while True:

    a = input("請輸入字串:")
    
    if a in keyword.kwlist:
        print(a,"是關鍵字")
    else:
        print(a,"不是關鍵字")

    if a == 'Q' or a == 'q':
        break 
