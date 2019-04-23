import speech_recognition as sr


def a2t():
    r = sr.Recognizer()
    with sr.WavFile("videos/audio.wav") as source:
        audio = r.listen(source)
    try:
        texts = r.recognize_google(audio)
        # print(texts)
        return texts
    except:
        return False
