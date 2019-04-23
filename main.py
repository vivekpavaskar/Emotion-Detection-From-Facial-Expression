import frameExtraction as fe
import keyFrameIdentifier as kfi
import analyseEmotionFromImage as aefi
import extractAudio as ea
import audioToText as att
import analyseEmotionFromText as aeft
from datetime import datetime as dt
# import extractROI as eroi


def startProject():
    # code for creating timestamp based directory in dataset
    dates = dt.now().strftime("%Y%m%d%H%M%S")

    # code for retrive data from DB

    # code for video path and status variable
    videoPath = 'videos/asd.mp4'
    statement = ""
    status = ""
    folder = "2"

    # Emotion From Video Frames
    # code for frame extraction function
    folder = fe.extractFrames(videoPath, dates)
    print(folder)
    # code for filtering key frames from frames
    kfi.filterKeyFrame(folder)
    # code for reading emotions from keyframes
    videoEmo = aefi.readEmotions(folder)
    print(videoEmo)

    # Emotion From Video Converted Audio
    # code for audio extraction
    audioPath = ea.v2a(videoPath)
    # code for audio to text
    audioToText = att.a2t()
    print(audioToText)
    # code for reading emotions from audio converted text
    if audioToText is not False:
        audioToText = 'dataset/text/all.txt'
        audioEmo = aeft.readEmotions(audioToText)
        print(audioEmo)

    # Emotion From Statement
    # code for reading emotions from statement
    # statementEmo = aeft.readEmotions(statement)
    # Decision Makaing

    # DB Updation

    return "completed"

startProject()
