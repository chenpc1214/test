def isTriangle(s1, s2, s3):
    if s1 + s2 < s3:
        return False
    if s1 + s3 < s2:
        return False
    if s2 + s3 < s1:
        return False
    return True

def area(s1, s2, s3):
    p = (s1 + s2 + s3) / 2
    return (p * (p - s1) * (p - s2) * (p - s3)) ** 0.5

d1, d2, d3  = eval(input("請輸入3個邊長 : "))

if isTriangle(d1, d2, d3):
    print("這是三角形的邊長")
    print("三角形面積是 : %8.3f" % area(d1,d2,d3))
else:
    print("這不是三角形的邊長")


"""自己寫的
def istriangle(s1,s2,s3):
    if s1+s2 > s3:
        print("yeah, it is triangle.")

def area(s1, s2, s3):
    p = (s1 + s2 + s3) / 2
    return (p * (p - s1) * (p - s2) * (p - s3)) ** 0.5

value = eval(input("please,enter the three sides of triangle:"))



if istriangle(value):
    print("right, it is triangle.")
else:
    print("no, it isn't triangle." )"""

