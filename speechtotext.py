import speech_recognition as sr


recognizer = sr.Recognizer()


with sr.Microphone() as source:
    print("Please say something...")


    recognizer.adjust_for_ambient_noise(source, duration=1)


    audio = recognizer.listen(source)


    try:

        text = recognizer.recognize_google(audio)
        print("You said: " + text)

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")

    except sr.RequestError:
        print("Could not request results from the service.")