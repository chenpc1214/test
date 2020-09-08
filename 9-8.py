
song = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""


songLower = song.lower()            


for ch in songLower:                
        if ch in ".,?":
            songLower = songLower.replace(ch,'')


songList = songLower.split()

dict = {wd:songList.count(wd) for wd in songList}
   
maxCount = max(dict.values())       
for key, count in dict.items():
    if count == maxCount:
        print("字串 %s 出現最多次共出現 %d 次" % (key, count))
