def calc(data, threshold, weight):
    total = 0
    result = 0
    perEmo = {"happy": 0, "sad": 0, "disgust": 0, "anger": 0, "fear": 0, "suprise": 0, "neutral": 0}

    for v in data.values():
        total = total + int(v)

    for e in data.keys():
        perEmo[e] = int(data[e]) / total * 100

    if perEmo["happy"] <= threshold["happy"]+2 or perEmo["happy"] <= threshold["happy"]-2:
        result = result + 1
    if perEmo["sad"] <= threshold["sad"]+2 or perEmo["sad"] <= threshold["sad"]-2:
        result = result + 1
    if perEmo["disgust"] >= threshold["disgust"]+2 or perEmo["disgust"] >= threshold["disgust"]-2:
        result = result + 1
    if perEmo["anger"] >= threshold["anger"]+2 or perEmo["anger"] >= threshold["anger"]-2:
        result = result + 1
    if perEmo["fear"] >= threshold["fear"]+2 or perEmo["fear"] >= threshold["fear"]-2:
        result = result + 1
    if perEmo["suprise"] <= threshold["suprise"]+2 or perEmo["suprise"] <= threshold["suprise"]-2:
        result = result + 1

    result = result / 6 * 100
    result = result * weight / 100
    return result


def decide(videoEmo, audioEmo, statementEmo):
    percentage = 0
    thersvideo = {"happy": 0.768087215, "sad": 27.89890981, "disgust": 0, "anger": 12.06640238, "fear": 7.061446977,
                  "suprise": 5.401387512, "neutral": 46.80376611}
    thersaudio = {"happy": 0.94543, "sad": 23.3387, "disgust": 0, "anger": 12.3987, "fear": 7.2663, "suprise": 5.2944,
                  "neutral": 50.7563}
    thersstatement = {"happy": 0.94543, "sad": 23.3387, "disgust": 0, "anger": 12.3987, "fear": 7.2663,
                      "suprise": 5.2944, "neutral": 50.7563}

    percentage = percentage + calc(videoEmo, thersvideo, 55)
    percentage = percentage + calc(audioEmo, thersaudio, 20)
    percentage = percentage + calc(statementEmo, thersstatement, 25)
    print(percentage)
    if percentage >= 60:
        return "Accepted"
    else:
        return "Rejected"

# videoEmo = {'happy': 0, 'sad': 46, 'disgust': 0, 'anger': 0, 'fear': 0, 'suprise': 0, 'neutral': 0}
# audioEmo = {'happy': 0, 'sad': 46, 'disgust': 0, 'anger': 0, 'fear': 0, 'suprise': 0, 'neutral': 0}
# statementEmo = {'happy': 0, 'sad': 46, 'disgust': 0, 'anger': 0, 'fear': 0, 'suprise': 0, 'neutral': 0}
# decide(videoEmo, audioEmo, statementEmo)
