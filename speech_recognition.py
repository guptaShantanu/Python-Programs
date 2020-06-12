import speech_recognition as sr

r=sr.recognizer()

with r.Microphone() as mr:
    audio=r.listen(mr)

    try:
        text=r.recognize_google(audio)
        print(text)
    except:
        print("cantpython")


