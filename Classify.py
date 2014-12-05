__author__ = 'davide'

'''
with open("list.txt") as f:
    content = f.readlines()
    with open("InternetThink.txt") as f:
        internet = f.readline()
        print(internet)
        for word in content:
            word = word.strip()
            # print(word)

            wordindex = internet.find(word)
            print(wordindex)

            try:
                with open("stemstop/" + word) as f:
                    content = f.readlines()
                sentenceArray = content
                #print(sentenceArray)
            except Exception as e:
                print(e)

'''

import os

pos_tweets = []
neg_tweets = []
ind_tweets = []

with open("internetnewline.txt") as f:
    content = f.readlines()
    list = []
    for word in content:
        success = "success\":1"
        if (success in word):
            # print(word)
            i = word.index("search\"")
            j = word.index("winner")
            parola = word[i + 9:j - 3]
            print(parola)

            i = word.index("winner\"")
            j = word.index(",\"positive")
            polarity = word[i + 9:j - 1]
            print(polarity)
            # list.append(polarity.replace("positive",'0').replace("negative",'1').replace("indifferent",'2'))

            # os.system("printf \"" + parola + "\n\" >> intwords.txt")
            try:
                with open("stemstop/" + parola) as f:
                    content = f.readlines()
                import re

                sentenceArray = content
                separator = "#"
                for s in sentenceArray:
                    s = s.replace("\n", '')
                    if ("neg" in polarity):
                        os.system("printf \"" + s + separator + "neg\n\" >> training_limited.csv")
                        #neg_tweets.append((s, 'negative'))
                    elif ("pos" in polarity):
                        os.system("printf \"" + s + separator + "pos\n\" >> training_limited.csv")
                        #pos_tweets.append((s, 'positive'))
                    elif ("ind" in polarity):
                        os.system("printf \"" + s + separator + "ind\n\" >> training_limited.csv")
                        #ind_tweets.append((s, 'indifferent'))
            except Exception as e:
                print(e)

'''
tweets = []
for (words, sentiment) in pos_tweets + neg_tweets + ind_tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweets.append((words_filtered, sentiment))





from sklearn import metrics



train_set = get_words_in_tweets(tweets)

def train_model(tweets, hashtags):
    train_set = features_from_tweets(tweets, hashtags)

    cv = cross_validation.KFold(len(train_set), n_folds=10)
    sum_accuracy = 0
    k = 0
    for traincv, testcv in cv:
        #classifier = nltk.NaiveBayesClassifier.train(train_set[traincv[0]:traincv[len(traincv)-1]])
        #classifier = nltk.MaxentClassifier.train(train_set[traincv[0]:traincv[len(traincv)-1]], max_iter=10)
        #classifier = nltk.SklearnClassifier(LogisticRegression()).train(train_set[traincv[0]:traincv[len(traincv)-1]])
        classifier = nltk.SklearnClassifier(LinearSVC()).train(train_set[traincv[0]:traincv[len(traincv)-1]])

        y_true = []
        y_pred = []
        for i in range(len(testcv)):
            y_true.append(train_set[testcv[i]][1])
            y_pred.append(classifier.classify(train_set[testcv[i]][0]))

        acc = metrics.accuracy_score(y_true, y_pred)
        sum_accuracy += acc

        k += 1
        print(str(k) + ')accuracy: ' + str(acc))
        print('true labels: ' + str(y_true))
        print('predicted labels: ' + str(y_pred))
        print('')
    print ('ACCURACY: ' + str(sum_accuracy/k))










'''
'''

def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


wordlist = get_words_in_tweets(tweets)
word_features = get_word_features(wordlist)


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


training_set = nltk.classify.apply_features(extract_features, tweets)
classifier = nltk.NaiveBayesClassifier.train(training_set)
print(classifier.show_most_informative_features(32))

'''