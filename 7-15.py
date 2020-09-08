buyers = [["Jamase",1030],["Curry",893],
          ["Durant",2050],["Jordan",990],
          ["David",2110],["Kevin",15000],
          ["Mary",10050],["Tom",8800],]

infinite = list()
VIP = list()
Gold = list()

while buyers:
    fall_out_buyer = buyers.pop()
    if fall_out_buyer[1] >= 10000:
        infinite.append(fall_out_buyer)
        
    elif 1000 <= fall_out_buyer[1] <= 10000:
        VIP.append(fall_out_buyer)

    else:
        Gold.append(fall_out_buyer)

print("infinite_buyers的資料:",infinite)
print("VIP_buyers的資料:",VIP)
print("Gold_buyers的資料:",Gold)
          
