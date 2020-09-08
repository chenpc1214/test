import re

passwords = {"amy":"cat152358646",
             "smallpie":"fg44565fgbg89425",
             "bob":"mypasss684126423",
             "ming":"613155364",
             "wang":"pp55",
             "angela":"ji32k7au4a83g4153"}

pattern = r"([A-Za-z]{1,}\d+\w+\d)"

for k,v in passwords.items():
    
    if len(v) >= 8:
        result = re.search(pattern,v)
        
        if result ==None:
            print("帳號:",k,"-------------->不合乎密碼規定")
        else:
            print("帳號:",k,"------------->密碼:",result.group())
        
           
    else:
        print("帳號:",k,"------------->密碼強度不足")



