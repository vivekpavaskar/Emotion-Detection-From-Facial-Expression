from moviepy.editor import *


def v2a(path):
    audioPath = "videos/audio.wav"
    video = VideoFileClip(path)
    audio = video.audio
    audio.write_audiofile(audioPath)
    return audioPath
