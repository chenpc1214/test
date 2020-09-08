noodles = {"牛肉麵":100,"肉絲麵":80,"陽春麵":60,"滷肉麵":90,"麻醬麵":70}

print(noodles)

for result,result2 in sorted(noodles.items(), key=lambda item:item[1]):
    print(result,  ":"  ,result2)
