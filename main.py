import frameExtraction as fe
import keyFrameIdentifier as kfi
import extractROI as eroi
import analyseEmotion as ae

if __name__ == '__main__':
    folder=fe.extractFrames()  # frame extraction function
    kfi.filterKeyFrame(folder)  # filtering key frames from frames
    # eroi.roi(folder)  # cropping roi from key frames
    ae.readEmotions() #reading emotions
