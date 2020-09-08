# ex6_5.py
sc1, sc2, sc3, sc4, sc5 = eval(input("請輸入5個考試成績 : "))
sc = [sc1,sc2,sc3,sc4,sc5]
print("分數串列       : ", sc)
print("高分往低分排列 : ", sorted(sc,reverse=True))
print("高分往低分排列 : ", sorted(sc))
print("最高分         : ", max(sc))
print("總分           : ", sum(sc))





  




    
