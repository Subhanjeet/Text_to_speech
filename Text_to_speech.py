import pyttsx3
print("Welcome to RoboSpeaker 1.1 Created by Subhanjeet")
engin = pyttsx3.init()
while True:
    x = input("Enter what you want to enter: ")
    if x.lower() == "stop":
        print("Thankyou for using")
        break
    engin.say(x)
    engin.runAndWait()