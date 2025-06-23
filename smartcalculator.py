import math

import speech_recognition as sr
import pyttsx3

def audii(sound):
    from gtts import gTTS


    import os
    language="hi"
    speech=gTTS(text=sound,lang=language,slow=False)
    speech.save("output.mp3")

    os.system("afplay output.mp3")


def audi(sound):
    engine = pyttsx3.init()
    voice=engine.getProperty("voices")
    engine.setProperty("voice", voice[5].name)
   # engine.save_to_file(sound,"vaibhav.waw")
    engine.say("Hello, this is a test.")
    engine.runAndWait()

def speech_recognize():
    recog=sr.Recognizer()

    with sr.Microphone() as source:
        recog.adjust_for_ambient_noise(source,duration=2)
        print("say something: ")
        try:
           audioo=recog.listen(source)
           txt=recog.recognize_google(audioo)
        except sr.WaitTimeoutError:
           print("retry and say something")
        except sr.UnknownValueError:
            print("i can't read that")
        finally:
            return txt

def numberextraction(text:str):
    l1=[]
    for t in text.split(" "):
        for e in t.split(","):
            try:
                l1.append(float(e))
            except ValueError:
                pass
    
    return l1

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def hcf(a,b):
    h=a if a>b else b
    while h>=1:
        if a%h==0 and b%h==0:
            return h
        h-=1

def lcm(a,b):
    l=a if a>b else b
    while l<=a*b:
        if l%a==0 and l%b==0:
            return l
        l+=1

def end():
    print("Thank you for Using smart calculator")
    input("press Enter key to exit")
    exit()
def sqrt(a):
    return a**0.5

def sorry():
    print("This Instruction is Beyond My ability")

operation0={
    "CLOSE":end,"END":end,"TERMINATE":end,"EXIT":end,"QUITE":end
}

operation1={"ROOT":sqrt}
operations2={
    "PLUS":add,"ADD":add,"SUM":add,"ADDITION":add,"SUM":add,"INCREASE":add,"TOTAL OF":add,"+":add,
    "MINUS":sub,"SUBSTRACT":sub,"DIFFERENCE":sub,"LESS":sub,"-":sub,"SUBTRACT":sub,
    "MULTIPLY":multiply,"PRODUCT":multiply,"*":multiply,"MULTIPLICATION":multiply,
    "DIVISION":divide,"DIVIDE":divide,"LCM":lcm,"HCF":hcf
    }

def main():
    print("welcome to smart calculator")
    while True:
        print()
        text=input("enter the input")
        print("You said: ",text)
        for word in text.split(" "):
            if word.upper() in operations2.keys():
                try:
                    l=numberextraction(text)
                    r=operations2[word.upper()](l[0]),l[1]
                    print("result ",r)
                except:
                    print("Someting is wrong please retry")
                finally:
                    break
            elif word.upper() in operation0.keys():
                operation0[word.upper()]()
                break
            elif word.upper() in operation1.keys():
                l=numberextraction(text)
                x=operation1[word.upper()](l[0])
                print("result is ", x)
                break
        else:
                sorry()


main()