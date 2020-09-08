your_url = input("請輸入網址:")

if your_url.startswith("http://"):
    print("網址正確")
elif your_url.startswith("https://"):
    print("網址正確")
else:
    print("沒有這東西")
