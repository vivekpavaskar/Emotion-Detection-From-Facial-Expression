import frameExtraction as fe
import keyFrameIdentifier as kfi
import extractROI as eroi
import analyseEmotion as ae

if __name__ == '__main__':
    # retrive data from DB

    # video path and status variable

    # Emotion From Video Frames
    # frame extraction function
    folder = fe.extractFrames()
    # filtering key frames from frames
    kfi.filterKeyFrame(folder)
    # cropping roi from key frames
    # eroi.roi(folder)
    # reading emotions
    ae.readEmotions()

    # Audio Extraction From Video

    # Audio To Text

    # Emotion From Text (statement and audio)


    #Decision Makaing


    #DB Updation