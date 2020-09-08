import re
 

def find(rule,something):

    result = re.search(rule,something)

    if result == None:
        print("字串搜尋失敗-----",result)
    else:
        print("字串搜尋成功-----",result.group())


msg = "son"
msg2 = "sonson"
msg3 = "sonsonson"
msg4 = "sonsonsonson"
msg5 = "sonsonsonsonson"

print("以下用son{2,}做測試")
rule = "(son){2,}"
find(rule,msg)
find(rule,msg2)
find(rule,msg3)
find(rule,msg4)
find(rule,msg5)
print("以下用son{,5}做測試")
rule = "(son){,5}"
find(rule,msg)
find(rule,msg2)
find(rule,msg3)
find(rule,msg4)
find(rule,msg5)
