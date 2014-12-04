from collections import defaultdict
from os.path import expanduser
import csv

import nltk
from sklearn import cross_validation
from sklearn.svm import LinearSVC
from sklearn import metrics


def read_file():
    home = expanduser("~")
    path_to_file = ""
    # file_name = "training.csv"
    #file_name = "training_uniform.csv"
    file_name = "training_limited.csv"
    with open(path_to_file + file_name, 'rb') as f:
        for row in csv.reader(f, delimiter='#', quoting=csv.QUOTE_ALL):
            #print(row)
            try:
                sentences.append(row[0])
                polar.append(row[1])
            except Exception as e:
                print(e)
                if ('neg' in row[0]):
                    polar.append('neg')
                if ('pos' in row[0]):
                    polar.append('pos')
                if ('ind' in row[0]):
                    polar.append('ind')


def unigrams(sentence):
    features = defaultdict(list)
    words = sentence.split()
    for w in words:
        features[w] = True
    return features


def feature_extractor(sentence):
    return unigrams(sentence)


def features_from_sentences(sentences, polar):
    feature_labels = []
    for i in range(len(sentences)):
        features = feature_extractor(sentences[i])
        feature_labels.append((features, polar[i]))
    return feature_labels


def train_model(sentences, polar):
    train_set = features_from_sentences(sentences, polar)

    cv = cross_validation.KFold(len(train_set), n_folds=10)
    sum_accuracy = 0
    k = 0
    for traincv, testcv in cv:

        # classifier = nltk.SklearnClassifier(naive_bayes.MultinomialNB()).train(train_set[traincv[0]:traincv[len(traincv)-1]])
        #classifier = nltk.MaxentClassifier.train(train_set[traincv[0]:traincv[len(traincv)-1]], max_iter=10)
        #classifier = nltk.SklearnClassifier(LogisticRegression()).train(train_set[traincv[0]:traincv[len(traincv)-1]])
        classifier = nltk.SklearnClassifier(LinearSVC()).train(train_set[traincv[0]:traincv[len(traincv) - 1]])
        shifters =
        y_true = []
        y_pred = []
        for i in range(len(testcv)):
            y_true.append(train_set[testcv[i]][1])
            label = classifier.classify(train_set[testcv[i]][0])
            # if any(word in 'some one long two phrase three' for word in list_):
            if any(parole in str(train_set[testcv[i]][0]) for parole in shifters):
                # if("saumya" in str(train_set[testcv[i]][0])):
                if (label == 0):
                    y_pred.append(1)
                elif (label == 1):
                    y_pred.append(1)
            else:
                y_pred.append(label)

        acc = metrics.accuracy_score(y_true, y_pred)
        sum_accuracy += acc

        k += 1
        print(str(k) + ')accuracy: ' + str(acc))
        print('true labels: ' + str(y_true))
        print('predicted labels: ' + str(y_pred))
        print('')

    print('ACCURACY: ' + str(sum_accuracy / k))





    # classifier.train(train_set)#aggiungere max_iter per maxent
    #return classifier


sentences = []
polar = []
read_file()
train_model(sentences, polar)

