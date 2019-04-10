import speech_recognition as sr

r = sr.Recognizer()

with sr.WavFile("videos/audio.wav") as source:
    print("Say something")
    audio = r.listen(source)
    print("Time Over, Thanks")

try:
    print("text: ", r.recognize_google(audio))
except:
    pass
