noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60,
           '大滷麵':90, '麻醬麵':70}
print(noodles)

maxPrice = max(noodles.values())       # 最貴的麵的價格
for key, price in noodles.items():
    if price == maxPrice:
        print("最貴的是   %s 金額是 %d" % (key, price))

minPrice = min(noodles.values())       # 最便宜的麵的價格
for key, price in noodles.items():
    if price == minPrice:
        print("最便宜的是 %s 金額是 %d" % (key, price))
