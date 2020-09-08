abc = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'
subText =abc[3:]+ abc[:3]
encry_dict = dict(zip(subText, abc))    
print("列印編碼字典\n", encry_dict)    

word ="I like python"
nothing = []

for word2 in word:
    nothing.append(encry_dict[word2])
    nothingtext = "".join(nothing)

print("原始字串:",word)
print("加密過的字串",nothingtext)

