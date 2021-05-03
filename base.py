# we're gonna make an AI today, bois. and it's gonna be the damn best AI of them all
# slave.hologram.iris. synchronous labyrinth for archived variable environments
# advanced, sonorous, trained evironmentally reliable indie s__ k__ asterisk

import speech_recognition as sr
import sys, os
from os import path
import time
import datetime
import webbrowser
from youtubesearchpython import SearchVideos
import random
import pyttsx3 as pyt3
import moviepy.editor as movpy 
from pytube import YouTube
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import playsound
import subprocess
import pathlib


#const
keyword = 'slave'

#tts.. FINALLY WOO
engine = pyt3.init('sapi5')
engine.setProperty('rate', 185)
osHomeDir = os.getcwd()

#voice commands to trigger effect

function_definitions = dict(
    youtube = [ 
        
        'search youtube for',
        'open youtube for',
        
    ],
    time = [

        'what time', 
        'say the time',
        'say the time right now',
        
    ],
    webSearch = [
        
        'search google for', 
        'google',
        
    ],
    how_are_you = [
        'tell me a fact',
        'are you real',
        'are you fake',
        'how was your day',
        'killed a man today',

    ],
    streamMusic = [

        'play song',
        'play music',
        
    ],


    open_application = [

        'open program',
        
        ],

    help = [
        'help'
    ]
    
)


#function dictionary. Use it to trigger functions

processor_definitions = dict(
    time = "tell_time",
    youtube = "open_youtube",
    webSearch = "search",
    how_are_you = "how_are_you", 
    streamMusic = "streamMusic",
    open_application = "open_application",
    help = "help",
)

# functions. 

#def voice_listen(): 
#
#    
#            return "None"
#        
#        return audioCommand.lower()


def tell_time(query):
    cur_time = datetime.datetime.now()
    hr_min = f'{cur_time.hour}:{cur_time.minute}'
    if cur_time.hour - 12 >= 0:
        engine.say(f'{hr_min} PM')
        engine.runAndWait()
    else:
        engine.say(f'{hr_min} AM')
        engine.runAndWait()
    
    # tts current time

def open_youtube(query):
    try:
        results = SearchVideos(str(query), max_results=1, mode='dict')
        engine.say(f"Opening video: {results.result()['search_result'][0]['title']}")
        engine.runAndWait()
        webbrowser.get().open(f"{results.result()['search_result'][0]['link']}")
    except:
        pass
        # print(0, Exception)
    #say opening {query}. witty remark

def search(query):
    engine.say(f"Searching google for {query}") # need to implement web scraping
    engine.runAndWait()
    webbrowser.get().open(f'https://www.google.com/search?q={query}')
    

def how_are_you(query):
    with open('qr.txt', 'r+') as f:
        data = f.readlines()
        for words in data:
            sentence = (data[random.randint(0,100)])
        f.close()
    
    with open ('qf.txt', 'r+') as f:
       data = f.readlines()
       for words in data:
           fact = (data[random.randint(0,100)])
       f.close()

    engine.say(f"{sentence}. Also here's a fact! Did you know? {fact}")
    engine.runAndWait()


def streamMusic(query): # get songs from pytube. lowest quality, covert into mp3..
    musicDir = (os.getcwd() + r'/tmp')
    os.chdir(musicDir)
    query = query[1:] # account for space in the pickup command
   
    engine.say(f"Streaming {query}. Please allow a few moments..")
    engine.runAndWait()

    results = SearchVideos(str(query), max_results=1, mode='dict')
    videoLink = (f"{results.result()['search_result'][0]['link']}")
    yt = YouTube(videoLink)
    ytVideo = yt.streams.filter(progressive = True).order_by('resolution').first()
    ytVideo.download(musicDir)

    
    for files in os.walk(musicDir):
        for filedir in files:
            for mp4 in filedir:
                if mp4.endswith('.mp4'): #verify file is actually of .mp4 extension
                    music = mp4
                    aClip = movpy.VideoFileClip(music).audio #select audio file 
                    aClip.write_audiofile(f"{music[0:-4]}.mp3") 
                    aClip.close() #write audio file as mp3 with the same name, and remove the '.mp4' section
                    os.remove(music) #Remove old .mp4 file
                    music = f"{music[0:-4]}.mp3"

    engine.say(f"Playing music {music}")
    engine.runAndWait()
    time.sleep(0.1)
    playsound.playsound(music)

    os.chdir(osHomeDir)


def open_application(query):
    programWorkingDirectory = r'C:/Users/Aone/AppData/Roaming/Microsoft/Windows/Start Menu/Programs'
    os.chdir(programWorkingDirectory)
    query = query[1:] + '.lnk'

    # print(query)
    try:
        for root, dirs, files in os.walk(programWorkingDirectory, topdown=False):
            for application in files:
                if application.lower() == query:
                    appLocation = (root+ '/' + application)
    
    except Exception as e:
        print(e)
    
    engine.say(f"Launching {query[:-4]}.")
    os.startfile(appLocation)

            
    os.chdir(osHomeDir)

def help(query):
    for k,v in function_definitions.items():
        print(f'Function: {k}, Command: {v}')




def processing(cmd): #main cpu for all process
    
    for k,v in function_definitions.items(): #access function_definitions{}
        for word in v:
            if cmd.lower().startswith(keyword) and word in cmd.lower(): #verify starts with trigger
                if processor_definitions[k]: #make sure func exists
                    cmd = cmd.replace(keyword, "") # remove keyword from cmd for the eval call
                    to_call = processor_definitions[k]
                    cmd = cmd[1:] # account for the [ word] space in command before picking it up
                    eval(to_call + '(cmd.replace(word,""))') #send func_call() to required function
                    break
                else:
                    #voice_listen()
                    pass
            #else:
                # print(cmd, v) # use for debug
            

if __name__ == "__main__": # initialize 
    
    engine.say(f"SLAVE protocol is ready. Listening for commands.")
    engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("")

        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration = 0.5)

        try:
            audioCommand = r.recognize_google(audio, language = 'en-in')
            print(">", audioCommand)
        except Exception as e:
            print(e, "\nUnable to recognize")

        processing(audioCommand)
    engine.stop()