import random

dice_list = []

for outside in range(1,6):
    for a in range(3):
        dice = random.randint(1,6)
        dice_list.append(dice)
    print("%d:隨機三組骰子的值:"%outside,sorted(dice_list))

    
    for a in range(3):
        dice_list.pop()
                
