import frameExtraction as fe
import keyFrameIdentifier as kfi
import analyseEmotionFromImage as aefi
import extractAudio as ea
import audioToText as att
import analyseEmotionFromText as aeft
import decisionMaking as dm


def startProject(data):
    # code for creating timestamp based directory in dataset
    dates=data["video"][:-4]
    # code for retrive data from DB

    # code for video path and status variable
    videoPath = 'videos/asd.mp4'
    statement = data["statement"]
    folder = ""

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
    # if audioToText is not False:
    #     audioToText = 'dataset/text/all.txt'
    #     audioEmo = aeft.readEmotions(audioToText)
    #     print(audioEmo)

    # Emotion From Statement
    # code for reading emotions from statement
    # statementEmo = aeft.readEmotions(statement)
    # Decision Makaing
    dm.decide(videoEmo,
              audioEmo={'happy': 0, 'sad': 46, 'disgust': 0, 'anger': 0, 'fear': 0, 'suprise': 0, 'neutral': 0},
              statementEmo={'happy': 0, 'sad': 46, 'disgust': 0, 'anger': 0, 'fear': 0, 'suprise': 0, 'neutral': 0})

    return "completed"


# startProject(0)
