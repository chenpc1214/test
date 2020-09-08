score = 87,99,69,52,78,98,80,92
list_score = list(score)

the_highest = max(score[:9])
the_lowest = min(score[:9])
total = sum(score[:9])
average = round(total/9,1)

print("最高分:",the_highest)
print("最低分:",the_lowest)
print("總分:",total)
print("平均:",average)
