import speech_recognition as sr


def a2t(path):
    r = sr.Recognizer()
    with sr.WavFile(path) as source:
        audio = r.listen(source)
    try:
        texts = r.recognize_google(audio)
        return texts
    except:
        return False
