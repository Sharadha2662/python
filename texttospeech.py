import pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 10)
voices = engine.getProperty('voices')
voice_choice = input("choose voice - Male(1) or Female(2): ")
if voice_choice == "1":
    engine.setProperty('voice', voices[0].id)
elif voice_choice == "2":
    engine.setProperty('voice', voices[1].id)
else:
    print("invalid choice! using default voice.")
    engine.setProperty('voice', voices[1].id)

text = input("enter the text you want to convert to speech: ")

engine.say(text)
engine.runAndWait()