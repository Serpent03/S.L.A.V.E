from pytube import YouTube
import os
import moviepy.editor as movpy
import playsound

pt = r'F:/Projects/S.L.A.V.E/tmp'

os.chdir(pt) #permanently change dir to temp folder

word = "f 14"
word = word.replace(" ", '')
musicList = []
alplist = ['(', ')', '-', '_', '[', ']', '{', '}', '+', ' ']

for cachedArray in os.walk(pt):
    for cachedFiles in cachedArray:
        for cacheMusic in cachedFiles:
            st = cacheMusic
            musicList.append(st)

for st in musicList:
    for char in st:
        if (char) in alplist:
            st = st.replace(char, '')
            if st.count(char) == 0:

                print(st)
            
    