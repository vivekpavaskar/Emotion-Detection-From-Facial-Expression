import nltk
from nltk.classify.naivebayes import NaiveBayesClassifier


def get_words_in_dataset(dataset):
    all_words = []
    for (words, sentiment) in dataset:
        all_words.extend(words)
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


def read_datasets(fname, t_type):
    data = []
    f = open(fname, encoding="utf8")
    for line in f:
        if line != '':
            data.append([line, t_type])
    f.close()
    return data


def extract_features(word_features, document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


def classify_dataset(word_features, classifier, data):
    return classifier.classify(extract_features(word_features, nltk.word_tokenize(data)))


def readEmotions(textdata):
    textEmo = {"happy": 0, "sad": 0, "disgust": 0, "anger": 0, "fear": 0, "suprise": 0, "neutral": 0}
    print("1")
    # read in joy , disgust, sadness, shame, anger, guilt, fear training dataset
    anger_feel = read_datasets('dataset/text/anger.txt', 'anger')
    disgust_feel = read_datasets('dataset/text/disgust.txt', 'disgust')
    fear_feel = read_datasets('dataset/text/fear.txt', 'fear')
    happy_feel = read_datasets('dataset/text/happy.txt', 'happy')
    neutral_feel = read_datasets('dataset/text/neutral.txt', 'neutral')
    sad_feel = read_datasets('dataset/text/sad.txt', 'sad')
    surprise_feel = read_datasets('dataset/text/surprise.txt', 'surprise')
    print("2")
    # filter away words that are less than 3 letters to form the training data
    data = []
    for (
            words,
            sentiment) in happy_feel + disgust_feel + surprise_feel + sad_feel + anger_feel + neutral_feel + fear_feel:
        words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
        data.append((words_filtered, sentiment))

    print("3")
    # extract the word features out from the training data
    word_features = get_word_features(get_words_in_dataset(data))

    print("4")
    # get the training set and train the Naive Bayes Classifier
    training_set = nltk.classify.util.apply_features(word_features, extract_features, data)
    classifier = NaiveBayesClassifier.train(training_set)

    print("5")
    # read in the test tweets and check accuracy
    anger_data = read_datasets(textdata, 'anger')
    disgust_data = read_datasets(textdata, 'disgust')
    fear_data = read_datasets(textdata, 'fear')
    happy_data = read_datasets(textdata, 'happy')
    neutral_data = read_datasets(textdata, 'neutral')
    sad_data = read_datasets(textdata, 'sad')
    surprise_data = read_datasets(textdata, 'suprize')
    # test_data.extend(read_datasets(textdata, 'sadness'))
    print("6")

    total = accuracy = float(len(anger_data))
    for data in anger_data:
        if classify_dataset(classifier, data[0]) != data[1]:
            accuracy -= 1
    print('Total accuracy anger: %f%% (%d/%d).' % (accuracy / total * 100, accuracy, total))
    textEmo["anger"] = accuracy

    total = accuracy = float(len(disgust_data))
    for data in disgust_data:
        if classify_dataset(data[0]) != data[1]:
            accuracy -= 1
    print('Total accuracy disgust: %f%% (%d/%d).' % (accuracy / total * 100, accuracy, total))
    textEmo["disgust"] = accuracy

    total = accuracy = float(len(fear_data))
    for data in fear_data:
        if classify_dataset(data[0]) != data[1]:
            accuracy -= 1
    print('Total accuracy fear: %f%% (%d/%d).' % (accuracy / total * 100, accuracy, total))
    textEmo["fear"] = accuracy

    total = accuracy = float(len(happy_data))
    for data in happy_data:
        if classify_dataset(data[0]) != data[1]:
            accuracy -= 1
    print('Total accuracy happy: %f%% (%d/%d).' % (accuracy / total * 100, accuracy, total))
    textEmo["happy"] = accuracy

    total = accuracy = float(len(neutral_data))
    for data in neutral_data:
        if classify_dataset(data[0]) != data[1]:
            accuracy -= 1
    print('Total accuracy neutral: %f%% (%d/%d).' % (accuracy / total * 100, accuracy, total))
    textEmo["neutral"] = accuracy

    total = accuracy = float(len(sad_data))
    for data in sad_data:
        if classify_dataset(data[0]) != data[1]:
            accuracy -= 1
    print('Total accuracy sad: %f%% (%d/%d).' % (accuracy / total * 100, accuracy, total))
    textEmo["sad"] = accuracy

    total = accuracy = float(len(surprise_data))
    for data in surprise_data:
        if classify_dataset(data[0]) != data[1]:
            accuracy -= 1
    print('Total accuracy surprise: %f%% (%d/%d).' % (accuracy / total * 100, accuracy, total))
    textEmo["suprise"] = accuracy

    return textEmo
