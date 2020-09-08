picture = ["da1.jpg","da2.jpng","da3.gif","da4.gif","da5.jpg","da6.jpg","da7.gif"]

gif = list()
jpng = list()
jpg = list()

for overall in picture:
    if overall.endswith(".gif"):
        gif.append(overall)
print("GIF的串列檔:",gif)

for overall in picture:
    if overall.endswith(".jpg"):
        jpg.append(overall)
print("JPG的串列檔:",jpg)

for overall in picture:
    if overall.endswith(".jpng"):
        jpng.append(overall)
print("JPNG的串列檔:",jpng)



