
def compareString(string):
    """檢查是否是搜尋的字串"""
    if string == searchStr:
        return True
    else:
        return False

def parseString(string):
    global num
    # notFoundSignal = True     # 註記沒有找到電話號碼為True
    for i in range(len(data)):  # 用迴圈逐步抽取字串長度做測試
        msg = data[i:i+len(string)]
        if compareString(msg):
            num += 1

fn = 'ex16_2.txt'
with open(fn) as file_obj:      # 讀取ex21_2.txt
    data = file_obj.read()

while True:
    searchStr = input("請輸入與搜尋字串 : ")
    num = 0
    parseString(searchStr)
    print("所搜尋字串 %s 共出現 %d 次" % (searchStr, num))
    print("\n是否繼續,輸入Y或y則程式繼續")
    again = input("= ")       # 讀取使用者輸入
    if again == 'Y' or again == 'y':    # 若輸入Y或y
        pass
    else:
        break
    


"""自己做的，有小錯(他會累加先前的結果)
import re, os

os.chdir(r"C:\Users\user\Desktop\Python 3.7\python王者歸來\解答")

num = 0

with open ("ex16_2.txt","rt") as file:
    data = file.read()

while True:
    
    sear = input("\n請輸入欲搜尋之字串:")
    rule = re.compile(sear)
    result = rule.findall(data)

    for final in result:
        num += 1
    
    print("所搜尋字串 %s 共出現 %d 次"%(sear,num),)

    conti = input("\n是否繼續,輸入Y或y:")

    if conti == "Y" or conti == "y":
        continue
    else:
        break
                                            """
        
 
