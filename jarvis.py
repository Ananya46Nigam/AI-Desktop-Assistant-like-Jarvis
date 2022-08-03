import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia as wk
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')#to take voices in desktop
voices=engine.getProperty("voices")
#print(voices) -to check how many voices in desktop

engine.setProperty('voice',voices[1].id) #0-male voice
#1-female voice
def speak(audio):
    engine.say(audio)
    engine.runAndWait()#waits for jarvis to finish speaking
    

def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if hour>0 and hour<12:
        speak("GoodMorning! Hope you have a great day ahead !")
        
    elif hour>12 and hour<16:
        speak("GoodAfternoon! How may I help you?")
        
    else:
        speak("Goodevening! I am always here to assist you!")
        
        
def takecommands():
    #takes microphone input given by user by speaking and returns string output 
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak ! Listening...")
        r.pause_threshold = 2 #seconds of non speaking audio before a phase is considered complete
        audio=r.listen(source)
        
    try:
        print("Recognising :-)")
        query= r.recognize_google(audio,language="en-in")
        print(f"You said :{query}\n")
    except Exception as e:
        #print(e)
        
        print("Pardon me.I didn't catch what you said.Come again?")
        return "None"
    return query

#for sendemail to work allow less secured apps in gmail
#and import smtplib
def sendemail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("ananyaextras@gmail.com","Ananya@123")
    server.sendemail("ananyaextras@gmail.com",to.content)
    server.close()
    
    
    
    
if __name__=="__main__":
    speak("Welcome to world of Artificial Intelligence")
    wishme()
    
while True:
    query=takecommands().lower()
    
    #logic for executing tasks based on query
    
    
    
    if "wikipedia" in query:
        speak("Searching Wikipedia !")
        query = query.replace("wikipedia","")
        result= wk.summary(query,sentences=2)
        speak("According to wikipedia..")
        print(result)
        speak(result)

    elif "open youtube" in query:
        speak("Enjoy youtube")
        webbrowser.open("http://www.youtube.com")
    elif "open google" in query:
        speak("Opening Google")
        webbrowser.open("http://www.google.com")
    elif "stack overflow" in query:
        webbrowser.open("http://www.stackoverflow.com")
    elif "play music" in query:
        speak("Enjoy some Music")
        webbrowser.open("http://www.jiosaavn.com")
    elif "watch movie" in query:
        speak("Opening Amazon prime video")
        webbrowser.open("https://www.primevideo.com/?ref_=dvm_pds_amz_in_as_s_g_176")
        
    # elif 'play music' in query:
    #         music_dir = 'D:\\Non Critical\\songs\\Favorite Songs'
    #         songs = os.listdir(music_dir)
    #         print(songs)    
    #         os.startfile(os.path.join(music_dir, songs[0]))
    
    elif "the time" in query:
        
        strtime=datetime.datetime.now().strtime("%H:%M:%S")
        speak(strtime)
    
    elif 'code' in query:
            codePath = "C:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
    elif "send email to ananya" in query:
        try:
            speak("What do you want to convey?")
            content= takecommands()
            to="ananyaextras@gmail.com"
            
            sendemail(to,content)
            speak("Email sent successfully")
            
            
        except Exception as e:
            print(e)
            speak("Sorry,could not send.")
            
    elif "quit" in query:
        speak("See you again soon! Goodbye....")
        exit(0)

    elif "shopping" in query:
        speak("Opening Amazon")
        webbrowser.open("http://www.amazon.in")
        
    elif "who are you" in query:
        speak("I am an AI assistant made by my mother Ananya Nigam at her home on third august twenty twenty two between 3 to 6 a.m.")
        
        
   #calculator
        
        
        
    elif "love you" in query:
        speak("And I love you till infinity")
        
    elif "idiot" in query:
        speak("Oops! I was told that my code is idiot-proof!")
        
        
    # else:
    #     speak("That is not a valid request.")
        