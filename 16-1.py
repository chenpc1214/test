import re

def chnumber(arg):
    a = re.compile(r"(\d{3})-(\d{4})-\d{4}")
    result = a.search(arg)
    return bool(result)


print("I love Taichung:是大陸手機號碼?",chnumber("I love Taichung"))
print("0932-999-199:是大陸手機號碼?",chnumber("0932-999-199"))
print("133-1234-1234:是大陸手機號碼?",chnumber("133-1234-1234"))
