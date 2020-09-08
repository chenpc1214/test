search = input("請輸入月份(例如1月):")

month ={"1月":"Jan","2月":"Feb",
        "3月":"Mar","4月":"Apr",
        "5月":"May","6月":"Jun",
        "7月":"Jul","8月":"Aug",
        "9月":"Sep","10月":"Oct",
        "11月":"Nov","12月":"Dec"}

if search in month:
    print(month[search])
else:
    print("輸入錯誤")
