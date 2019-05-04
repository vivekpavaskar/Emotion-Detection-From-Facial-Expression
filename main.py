import frameExtraction as fe
import keyFrameIdentifier as kfi
import analyseEmotionFromImage as aefi
import extractAudio as ea
import audioToText as att
import analyseEmotionFromText as aeft
import decisionMaking as dm


def startProject(data):
    # code for creating timestamp based directory in dataset
    dates = data["video"][:-4]

    # code for video path and status variable
    videoPath = '../SHHP/storage/videoData/' + dates + '.mp4'
    statement = data["statement"]
    # folder='20190502085529'

    # Emotion From Video Frames
    print(1)
    # code for frame extraction function
    folder = fe.extractFrames(videoPath, dates)

    print(2)
    # code for filtering key frames from frames
    kfi.filterKeyFrame(folder)

    print(3)
    # code for reading emotions from keyframes
    videoEmo = aefi.readEmotions(folder)

    # Emotion From Video Converted Audio

    print(4)
    # code for audio extraction
    audioPath = ea.v2a(videoPath)

    print(5)
    # code for audio to text
    audioToText = att.a2t(audioPath)

    print(6)
    # code for reading emotions from audio converted text
    if audioToText is not False:
        audioToText = 'dataset/text/all.txt'
        audioEmo = aeft.readEmotions(audioToText)
        print(audioEmo)
    else:
        audioEmo = False
    # Emotion From Statement

    print(7)
    # code for reading emotions from statement
    statementEmo = aeft.readEmotions(statement)

    print(8)
    # Decision Makaing
    decision = dm.decide(videoEmo, statementEmo, audioEmo)
    # decision ="hjb"
    return decision

# startProject(0)
