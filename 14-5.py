
srcFn = input("請輸入來源檔案 : ")
dstFn = input("請輸入目的檔案 : ")        
with open(srcFn) as src_Obj:        # 用預設mode=r開啟檔案,傳回檔案物件src_Obj
    data = src_Obj.read()           # 讀取檔案到變數data

with open(dstFn, 'w') as dst_Obj:   # 開啟檔案mode=w
    dst_Obj.write(data)             # 將data輸出到檔案


"""自己做的

a = input("請輸入來源檔:")
b = input("請輸入目的檔:")

import shutil

shutil.copy(a,b)"""
