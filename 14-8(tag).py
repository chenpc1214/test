fn = 'ex14_6_1.txt'         # 設定欲開啟的檔案
with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    for line in file_Obj:   # 逐行讀取檔案到變數line
        print(line)         # 輸出變數line相當於輸出一行




"""自己做的
with open ("ex14_6_1.txt","rt") as name:
    data = name.readlines()
    print(data)"""


