search = input("請輸入星期幾的英文:")

e = {"Monday":"星期一" ,
     "Tuesday":"星期二",
     "Wensday":"星期三",
     "Thursday":"星期四",
     "Friday":"星期五",
     "Saturday":"星期六",
     "Sunday":"星期日"}

if search.title() in e:
    print(e[search.title()])
else:
    print("輸入錯誤")

    
