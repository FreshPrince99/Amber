import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes



listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

talk("Hey there! I'm Amber. Your very own virtual assistant. How may I help you?")

def take_cmd():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'zeppeli' in command:
                command= command.replace('zeppeli','')
                print(command)
            else:
                talk("How could you forget my name?")

    except:
        pass

    return command

def run_amber():
    command=take_cmd()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)



    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('Current time is'+time)



    elif 'search for' in command:
        data= command.replace('search for','')
        info=wikipedia.summary(data,2)
        print(info)
        talk(info)



    elif 'joke' in command:
        joke=pyjokes.get_joke()
        talk(joke)


    elif 'whatsapp' in command:
        talk("Tell me the message you want to send")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                voice = listener.listen(source)
                message = listener.recognize_google(voice)
                message = message.lower()
        except:
            pass
        print(message)

        talk("Which number would you like to send it to")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                voice = listener.listen(source)
                num = listener.recognize_google(voice)
        except:
            pass

        num=num.replace(" ",'')
        num='+91'+num
        print(num)

        cur_hour=int(datetime.datetime.now().strftime("%H"))
        cur_min=int(datetime.datetime.now().strftime("%M"))+1

        pywhatkit.sendwhatmsg(num,message,cur_hour,cur_min)


    elif 'exit' in command:
        talk("Bye! see you later")
        global flag
        flag=False

    else:
        talk("Could you repeat your statement?")


flag=True
while flag==True:
    run_amber()

        
