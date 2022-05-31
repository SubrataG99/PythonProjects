
# Create a Virtual Assistant

#------------------------------------------------------------------Imports
# import imtplib        # needed for the sending mail part
import pyttsx3
import speech_recognition as sr
import time
import os
import datetime
import wikipedia
import webbrowser
import random
import pyjokes
import sys
import pywhatkit
from subprocess import *
from random_word import RandomWords
from quote import quote
import requests
import randfacts
import geocoder
import socket

#------------------------------------------------------------------Creating Engine
eng = pyttsx3.init('sapi5')
voice = eng.getProperty('voices')
eng.setProperty('voice', voice[0].id)

#------------------------------------------------------------------Speak Function
def speak(audio, speed=200):
    eng.setProperty('rate', speed)
    eng.say(audio)
    eng.runAndWait()

#------------------------------------------------------------------Intro & Extra non working feature (Voice Authentication)
def Intro():
    hr = int(datetime.datetime.now().hour)
    if hr > 0 and hr < 12 :
        print('Good Morning User !')
        speak('Good morning User')
    elif hr > 12 and hr < 16 :
        print('Good Afternoon User !')
        speak('Good afternoon User')
    elif 16 < hr < 21 :
        print('Good Evening User !')
        speak('Good evening User')
    elif 21 < hr < 24 :
        print('Its almost time to sleep dear User, but i am here to help you !')
        speak('Its almost time to sleep dear User, but i am here to help you')
    print('Wait a minute, Who are you ?')
    speak('Wait a minute')
    speak('Who are you', 100)
    # print('Your Voice ID please')
    # speak('Let me hear your voice at first')
    time.sleep(3)
    print('Voice identification complete !')
    speak('Voice identication complete', 180)
    print('Welcome SG !!!')
    speak('Welcome SG')
    time.sleep(0.3)
    print('I am your Virtual Assistant...')
    speak('I am your virtual assistant')
    print('How can i help you sir ?')
    speak('How can i help you sir ?')

#------------------------------------------------------------------Taking Voice commands from Microphone
def VoiceCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print('\nI am Listening...')
        speak('I am Listening')
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing command')
        query = r.recognize_google(audio, language='en-in')
        print('You said :', query)
        # speak(query)
    except Exception as e:
        print(e)
        print('I am sorry but i dont understand')
        print('Say that again please')
        speak('Can you please repeat again ?')
        return 'None'
    return query

#------------------------------------------------------------------Weather API
# def weather(place):
#     BaseURL = 'http://api.openweathermap.org/data/2.5/weather?'
#     place = ''
#     ApiKey = '33029ab51f80643ee58e078b1c77587f'
#     Url = BaseURL + 'q=' + place + '&appid' + ApiKey
#     response = requests.get(Url)
#     if response.status_code == 200 :
#         data = response.json()
#         main = data['main']
#         temperature = main['temp']
#         humidity = main['humidity']
#         pressure = main['pressure']
#         report = data['weather']
#         print(f'{place:-^30}')
#         print(f'Temperature : {temperature}')
#         print(f'Humidity : {humidity}')
#         print(f'Pressure : {pressure}')
#         print(f'Weather Report : {report[0]["description"]}')
#     else :
#         print('Error in HTTP request...')

def clr():
    os.system('cls')

def stopwatch():
    t = (h*60*60) + (m*60) + s
    hh = 0
    mm = 0
    ss = 0
    for i in range(t):
        if 'stop' in task:
            break

        if ss==59:                                                                  # Changing seconds to next minute
            ss = 0
            mm = mm + 1
        else:
            ss = ss + 1
        
        if mm==59:                                                              # Changing minutes to next hour
            mm = 0
            hh = hh + 1
        
        print('Time elapsed ==>', hh, 'hr :', mm, 'min :', ss, 'sec')
        time.sleep(1)
        clr()
    print('Total time :', hh, 'hr :', mm, 'min :', ss, 'sec')
    print('Time up...!!!\n')
    speak('Total time elapsed is', hh, 'hours', mm, 'minutes', ss, 'seconds')

def countdown(h, m, s):
    t = (h*60*60) + (m*60) + s
    hh = h
    mm = m
    ss = s
    for i in range(t):
        if ss==0:
            ss = 59
            mm = mm - 1
        else:
            ss = ss - 1
        
        if mm==0 and hh>0:
            mm = 59
            hh = hh - 1
        
        print('Time elapsed ==>', hh, 'hr :', mm, 'min :', ss, 'sec')
        time.sleep(1)
        clr()
    print('Time up...\n')
    speak('Your time of', h, 'hours', m, 'minutes and', s, 'seconds is up')

#------------------------------------------------------------------###########-------------------------------------Main Function
if __name__ == '__main__':
    cnt = 0
    print('\nInitiating AI interface')
    speak('Initiating AI interface', 190)
    time.sleep(0.5)
    Intro()
    while True :
        task = VoiceCommand().lower()
        if 'who is' in task :                                                                # Wikipedia 
            print('Searching online...')
            speak('Searching online')
            task = task.replace('who is', '')
            out = wikipedia.summary(task, sentences=2)
            speak('According to Wikipedia')
            print('\n', out)
            speak(out)

#-----------------------------------------------------------------------------------------------------------------------------------
        elif 'open youtube' in task :                                                         # Opening YT
            webbrowser.open('youtube.com')

#-----------------------------------------------------------------------------------------------------------------------------------
        elif 'open google' in task :                                                           # Opening Google
            webbrowser.open('google.com')

#-----------------------------------------------------------------------------------------------------------------------------------
        elif 'play music' in task :                                                            # Playing songs
            # musicDir = 'D:\\Songs'
            # song = os.listdir(musicDir)
            # temp = random.randint(0, len(song)-1)
            # os.startfile(os.path.join(musicDir, song[temp]))
            # print('Playing', song[temp])
            print('No songs available')
            speak('No songs found in local device')

#-----------------------------------------------------------------------------------------------------------------------------------
        elif 'date today' in task :                                                         # Show date
            today = datetime.date.today()
            today = today.strftime("%d %B %Y")
            print('Today is :', today)
            speak('Todays date is' + today)
            CurrDate = datetime.date.today().strftime('%A')
            print('and the day is :', CurrDate)
            speak('and the day is' + CurrDate)

#-----------------------------------------------------------------------------------------------------------------------------------
        elif 'time now' in task :                                                           # Show time
            strTime = datetime.datetime.now().strftime('%I : %M : %S %p')
            print('The current time is :', strTime)
            speak('The current time is' + strTime)
        
#-----------------------------------------------------------------------------------------------------------------------------------
        elif 'date and time' in task :                                                      # Show date and time both
            today = datetime.date.today()
            today = today.strftime("%d %B %Y")
            print('Today is :', today)
            speak('Todays date is' + today)
            strTime = datetime.datetime.now().strftime('%I : %M : %S %p')
            print('The current time is :', strTime)
            speak('The current time is' + strTime)            

#-----------------------------------------------------------------------------------------------------------------------------------
        elif 'yourself' in task :                                                            # Introduction about the assistant
            print('Hello, User... Let me introduce myself... I am,')
            speak('Hello user, Let me introduce myself, I am')
            print('Virtual (V)')
            speak('Virtual', 220)
            print('Assistant (A)')
            speak('Assistant', 220)
            print('Artificial (A)')
            speak('Artificial', 220)
            print('Intelligence (I)')
            speak('Intelligence', 210)
            print('collectively called as VAAI. I am a simple AI system built by SG with help from internet.')
            speak('collectively called as bhai  I am a simple AI system built by SG with help from internet', 198)
            print('I am able to perform a lot of tasks and many more to come in future maybe.')
            speak('I am able to perform a lot of tasks and many more to come in future maybe')
            print('But for now i can do the following tasks :')
            speak('but for now i can do the following tasks')
            print('--> Tell you a joke')
            speak('Tell you a joke', 210)
            print('--> Tell you a quote')
            speak('Tell you a quote', 210)
            print('--> Tell you a random fact')
            print('--> Tell you present date or time or both')
            speak('tell you present date, or time, or both', 209)
            speak('Tell you a random fact', 210)
            print('--> Show weather of any place you want')
            speak('Show weather of any place you want', 210)
            print('--> Details of user (you)')
            speak('Details of user, it is you in this case', 210)
            print('--> Play music')
            speak('play music from local storage or from youtube', 210)
            print('--> Search on Wikipedia')
            speak('Search on Wikipedia', 210)
            print('--> Help you decide by tossing a coin')
            speak('Help you decide by tossing a coin', 210)
            print('--> Roll a dice for multiple choices')
            speak('Roll a dice for multiple choices')
            time.sleep(4)
            print('I dont have any competitors because i know i am the best...!')
            speak('I dont have any competitors because i know i am the best')

#-----------------------------------------------------------------------------------------------------------------------------------
        elif 'mail to' in task :                                                              # mail to someone
            # try :
            #     print('What should i say sir ?')
            #     speak('What should i say sir')
            #     content = VoiceCommand()
            #     print('To whom ?')
            #     speak('Who will this mail deliver to')
            #     to = VoiceCommand()
            #     to = to + '@gmail.com'
            # except :
            #     print('Sorry, this email failed to reach to its destination')
            #     speak('Sorry, this mail failed to reach to its destination')
            # server = imtplib.SMTP('smtp.gmail.com', 587)
            # server.echo()
            # server.starttls()
            # server.login('youremail@gmail.com', 'password')
            # server.sendmail('youremail@gmail.com', to, content)
            # server.close()
            print('Under development')
            speak('Sorry for the inconvenience, this feature is still not available, but will at your fingertips soon', 185)

#-----------------------------------------------------------------------------------------------------------------------------------
        elif 'game' in task :                                                               # play a game
            speak('Sure sir')
            print('Controls :')
            speak('Let me show you the controls', 190)
            print('UP ARROW to move forward')
            speak('Up arrow to move forward')
            print('DOWN ARROW to move down/back')
            speak('Down arrow to move backward or down')
            print('LEFT ARROW to move left')
            speak('Left arrow to move left')
            print('RIGHT ARROW to move right')
            speak('Right arrow to move right')
            speak('Game starting in')
            print('3...', end='\t')
            speak('3', 180)
            print('2...', end='\t')
            speak('2', 180)
            print('1...')
            speak('1')
            print('Enjoy !')
            speak('Enjoy the game sir')
            Popen('python SnakeGameGFG.py')                                             # execute file 'SnakeGameGFG.py'

   #-----------------------------------------------------------------------------------------------------------------------------------     
        elif 'coin' in task :
            temp = random.randint(0, 1)
            if temp == 0 :
                print('HEADS')
                speak('You got Head in toss')
            else :
                print('TAILS')
                speak('You got Tail in toss')

#-----------------------------------------------------------------------------------------------------------------------------------    
        elif 'set timer' in task :
            print('What type of Timer do you want...?')
            speak('What type of timer do you want...?')
            print('Stopwatch')
            time.sleep(0.4)
            print('Countdown')
            speak('Stopwatch, or Countdown timer?')
            if 'Countdown' in task:                                                                             # calls Countdown timer
                print('Enter the hours : ')
                speak('Enter the hours')
                h = VoiceCommand().lower()
                print('Enter the minutes :')
                speak('Enter the minute')
                m = VoiceCommand().lower()
                print('Enter the Seconds :')
                speak('Enter the seconds')
                s = VoiceCommand().lower()
                countdown(h, m, s)
            elif 'Stopwatch' in task:                                                                           # calls Stopwatch
                stopwatch()
            else:
                print('I think your audio is not clear or you are asking for any wrong option...')
                speak('I think your audio is not clear or you are asking for any wrong option', 185)

#-----------------------------------------------------------------------------------------------------------------------------------
        elif 'dice' in task :                                                               # roll a dice
            temp = random.randint(1, 6)
            print('Its a', temp)
            speak('Its a' + str(temp))
#-----------------------------------------------------------------------------------------------------------------------------------
        elif 'quote' in task :                                                              # Random Quotes
            auth = ''
            quot = ''
            r = RandomWords()
            w = r.get_random_words()
            if w == None:
                w = ['fire', 'air', 'water', 'earth', 'man', 'words', 'ability', 'adapt', 'forget', 'fear', 'love', 'see', 'success', 'motivation', 'fun', 'power', 'hope', 'sadness', 'happiness', 'wisdom', 'Truth', 'academic', 'reality']
                auth = 'Anynomous'
            temp = random.randint(0, len(w)-1)
            res = quote(w[temp], limit=1)
            for i in range(len(res)):
                quot = quot + res[i]['quote']
                auth = auth + res[i]['author']
                print(quot)
                print('\t\t--by', auth)
                speak(auth + 'said in one of their quotes')
                speak(quot, 150)
            cnt += 1
            if cnt > 3 :                                                    # asking if you are depressed
                print('Are you OK ?')
                speak('By the way, are you really ok')
                print('Should i call for help ?')
                speak('Should i call for online help')
                ch = VoiceCommand()
                if ch == 'no' :
                    print('Connecting to Depression helpline numbers')
                    speak('Connecting to Depression helpline numbers', 240)
                else :
                    print('Great ! Keep fighting')
                    speak('Great, keep fighting boss')

#-----------------------------------------------------------------------------------------------------------------------------------
        elif 'weather' in task :                                                               # Weather of a Place
            print('I beg your pardon \nWeather of which place...?')
            speak('Can you specify the name of the place again please ?')
            place = VoiceCommand()
            BaseURL = 'http://api.openweathermap.org/data/2.5/weather?'
            ApiKey = 'd8c632ea3787bd0811865599f8c7306f'                     ### Temporary maybe just for a day
            Url = BaseURL + 'q=' + place + '&appid' + ApiKey
            response = requests.get(Url)
            if response.status_code == 200 :
                data = response.json()
                main = data['main']
                temperature = main['temp']
                humidity = main['humidity']
                pressure = main['pressure']
                report = data['weather']
                print(f'{place:-^30}')
                speak('The weather forecast at {} is'.format(place))
                print(f'Temperature : {temperature}')
                speak('The temperature is' + temperature)
                print(f'Humidity : {humidity}')
                speak('Humidity =' + humidity)
                print(f'Pressure : {pressure}')
                speak('Pressure =' + pressure)
                print(f'Weather Report : {report[0]["description"]}')
                speak(report[0]['description'])
            else :
                print('Error in HTTP request...')
                speak('Sorry could not connect for weather')

#-----------------------------------------------------------------------------------------------------------------------------------
        elif 'play' in task :                                                                  # Playing Song/Video
            print(task)
            task = task.replace('play', '')
            print('Playing', task)
            speak('Playing', task)
            pywhatkit.playonyt(task)

#-----------------------------------------------------------------------------------------------------------------------------------    
        elif 'details' in task :                                                            # User location & details
            host = socket.gethostname()
            ipadd = socket.gethostbyname(host)
            print('Your device is : ', host)
            speak('The device you are using is')
            speak(host, 170)
            print('Your IP address is :', ipadd[:5])
            speak('Your IP address is')
            speak('Keep it hidden for privacy purpose')
            g = geocoder.ip('me')
            LatLong = g.latlng
            if LatLong[0] > 0 :
                Latdir = 'N'
                LatdirName = 'North'
            else :
                Latdir = 'S'
                LatdirName = 'South'
            if 0 < LatLong[1] < 180 or -180 < LatLong[1] < 0 :
                if LatLong[1] > 0 :
                    LongDir = 'E'
                    LongDirName = 'East'
                else :
                    LongDir = 'W'
                    LongDirName = 'West'
            else :
                LongDir = 'W'
                LongDirName = 'West'
            # print(LatLong)
            print('Latitude :', LatLong[0], Latdir)
            speak('Latitude at your location is' + str(LatLong[0]) + LatdirName)
            print('Longitude :', LatLong[1], LongDir)
            speak('and Longitude at your location is' + str(LatLong[1]) + LongDirName)

#-----------------------------------------------------------------------------------------------------------------------------------    
        elif 'fact' in task :                                                               # Random Fact
            print("Here's a wonderful fact for you sir...")
            speak("Here's a wonderful fact for you sir")
            fact = randfacts.get_fact(False)
            print(fact)
            speak(fact, 190)

#-----------------------------------------------------------------------------------------------------------------------------------
        elif 'joke' in task :                                                                # Jokes
            print('I got you a good one, Listen to it\n')
            speak('I got you a good one, Listen to it')
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

#-----------------------------------------------------------------------------------------------------------------------------------
        elif 'shut down' in task :                                                          # Deactivating/Shut down Jarvis
            print("Happy to help you...")
            speak('Happy to help you')
            print('See you soon sir\nwith lots of new functions for you')
            speak('See you next time with more functions for you', 190)
            sys.exit()
