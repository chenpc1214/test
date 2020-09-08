cocktail = {
    'Blue Hawaiian':{'Rum','Sweet Wine','Cream','Pineapple Juice','Lemon Juice'},
    'Ginger Mojito':{'Rum','Ginger','Mint Leaves','Lime Juice','Ginger Soda'},
    'New Yorker':{'Whiskey','Red Wine','Lemon Juice','Sugar Syrup'},
    'Bloody Mary':{'Vodka','Lemon Juice','Tomato Juice','Tabasco','little Sale'},
    "Horse's Neck":{'Brandy','Ginger Soda'},
    'Cosmopolitan':{'Vodka','Sweet Wine','Lime Juice','Cranberry Juice'},
    'Sex on the Beach':{'Vodka','Peach Liqueur','Orange Juice','Cranberry Juice'}
    }


print("含有Vodka的酒 : ")
for a,b in cocktail.items():
    if "Vodka" in b:
        print(a)


print("含有Sweet Wine的酒 : ")
for key,value in cocktail.items():
    if "Sweet Wine" in value:
        print(key)
        
print("含有Vodka和Cranberry Juice的酒 : ")
for k,v in cocktail.items():
    if "Vodka" and "Cranberry Juice" in v:
        print(k)
        
print("含有Vodka但是沒有Cranberry Juice的酒 : ")
for k2,v2 in cocktail.items():
    if "Vodka" in v2 and  not ('Cranberry Juice' in v2):
        print(k2)
