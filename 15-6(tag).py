import os
os.chdir("C:\\Users\\user\\Desktop\\Python 3.7\\python王者歸來\\解答")

def wordsNum(fn):
    
    try:
        with open(fn) as file_Obj:
            data = file_Obj.read()  
    except FileNotFoundError:
        print("找不到 %s 檔案" % fn)
    else:
        wordList = data.split()     
        print(fn, " 文章的字數是 ", len(wordList))    
        return len(wordList)

def lenWord(fn):
    
    wdlen = wordsNum(fn)                              
    if wdlen < 10:                                              
        raise Exception('檔案長度不足')
    if wdlen > 35:                                    
        raise Exception('檔案長度太長')
    print('檔案長度正確')

for file in ("d1.txt","d2.txt","d3.txt","d4.txt","d5.txt"):  
    try:
        lenWord(file)
    except Exception as err:
        print("檔案長度檢查異常發生: ", str(err))





"""自己做的

def open_file(arg):

    with open (str(arg),"rt") as name:
            data = name.read()
            b = data.split()
            c = len(b)
            
            if c > 35 :
                raise Exception("檔案長度太長")
            if c < 8 :
                raise Exception("檔案長度太短")

        
sth_list = ["d1.txt","d2.txt","d3.txt","d4.txt","d5.txt"]


try:
    
    for result in sth_list:
        open_file(result)
        b = data.split()
        c = len(b)
        print("%s  文章的字數是 %d 個字" %(result,c))

except Exception as err:
    print("檔案檢常長度發生異常:", str(err))"""
    
