lyric = """Are you sleeping, are you sleeping, Brother John, Brother John
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong"""

print("歌曲字串內容")
print(lyric.replace(",",""))

print("歌曲串列內容")
lowerlyric = lyric.lower()
lowerlyricsplit = lowerlyric.split()
print(lowerlyricsplit)

print("歌曲總字數:",len(lowerlyricsplit))
words = input("請輸入想找的字串:")
times = lowerlyricsplit.count(words)
print("%s出現的次數為%d"%(words,times))
    
