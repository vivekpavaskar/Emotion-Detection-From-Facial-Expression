from moviepy.editor import *
video = VideoFileClip("videos/testt.mp4")
audio = video.audio
audio.write_audiofile("videos/audio.wav")