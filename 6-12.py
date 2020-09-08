a = "Mary","Josh","Tracy"
name = list(a)
print("目前宴會名單:",name)

choice = input("""(1)增加名單
(2)刪除名單
=""")

if eval(choice)==1:
    add = input("請輸入人名:")
    name.append(add)
    print("新的宴會名單:",name)
elif eval(choice)==2:
    slash = input("請輸入將除名的人:")
    name.remove(slash)
    print("經刪減過後的名單:",name)
else:
    print("請認真輸入")
    
