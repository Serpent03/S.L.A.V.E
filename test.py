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
            
num=int(input("Enter the number of people: "))
count=1
people=dict()
for count in range(num):
    name=input("name: ")
    phone_number=input("phone number: ")
print("\n\nName\tPhone Number")
for num in people:
    print(num,'\t\t',phone_number[num])

