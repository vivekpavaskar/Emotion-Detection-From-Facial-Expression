import frameExtraction as fe
import keyFrameIdentifier as kfi
import extractROI as eroi
import analyseEmotion as ae
import extractAudio as ea
import audioToText as att

if __name__ == '__main__':
    # retrive data from DB
    # video path and status variable
    videoPath = 'videos/testt.mp4'
    status = ""

    '''
    # Emotion From Video Frames
    # frame extraction function
    folder = fe.extractFrames(videoPath)
    print(folder)

    # filtering key frames from frames
    kfi.filterKeyFrame(folder)
    
    # cropping roi from key frames
    # eroi.roi(folder)
    # reading emotions
    videoEmo=ae.readEmotions()
    print(videoEmo)
    # Audio Extraction From Video
    audioPath = ea.v2a(videoPath)
    '''
    # Audio To Text
    audioToText=att.a2t()
    # Emotion From Text (statement and audio)

    # Decision Makaing

    # DB Updation
