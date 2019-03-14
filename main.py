import frameExtraction as fe
import keyFrameIdentifier as kfi
import extractROI as eroi

if __name__ == '__main__':
    # fe.extractFrames()  # frame extraction function
    kfi.filterKeyFrame()  # filtering key frames from frames
    # eroi.roi()  # cropping roi from key frames
