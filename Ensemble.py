from collections import defaultdict
from os.path import expanduser
import csv

import nltk
from sklearn import naive_bayes
from sklearn import cross_validation
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn import metrics


def read_file():
    home = expanduser("~")
    path_to_file = ""
    # file_name = "training.csv"
    # file_name = "training_uniform.csv"
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


def Counter(a):
    from collections import Counter

    b = Counter(a)
    # print (b.most_common(1))
    if ('1' in str(b.most_common(1))):
        return a[0]
    if ('pos' in str(b.most_common(1))):
        return 'pos'
    if ('neg' in str(b.most_common(1))):
        return 'neg'
    if ('ind' in str(b.most_common(1))):
        return 'ind'


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
    sum_accuracy1 = 0
    sum_accuracy2 = 0
    sum_accuracy3 = 0
    sum_accuracy4 = 0
    sum_accuracy5 = 0
    sum_accuracy6 = 0
    sum_accuracy7 = 0
    sum_accuracy8 = 0

    k = 0

    for traincv, testcv in cv:

        classifier1 = nltk.SklearnClassifier(naive_bayes.MultinomialNB()).train(
            train_set[traincv[0]:traincv[len(traincv) - 1]])
        classifier2 = nltk.MaxentClassifier.train(train_set[traincv[0]:traincv[len(traincv) - 1]], max_iter=10)
        classifier3 = nltk.SklearnClassifier(LogisticRegression()).train(
            train_set[traincv[0]:traincv[len(traincv) - 1]])
        # classifier = nltk.SklearnClassifier(DecisionTreeClassifier()).train(train_set[traincv[0]:traincv[len(traincv) - 1]])
        classifier4 = nltk.SklearnClassifier(LinearSVC()).train(train_set[traincv[0]:traincv[len(traincv) - 1]])
        #'no','not','yet','never','none','nobody','nowhere','nothing','neither'
        #shifters = []
        y_true = []
        y_pred1 = []
        y_pred2 = []
        y_pred3 = []
        y_pred4 = []
        y_pred5 = []
        y_pred6 = []
        y_pred7 = []
        y_pred8 = []
        for i in range(len(testcv)):
            y_true.append(train_set[testcv[i]][1])
            label1 = classifier1.classify(train_set[testcv[i]][0])
            label2 = classifier2.classify(train_set[testcv[i]][0])
            label3 = classifier3.classify(train_set[testcv[i]][0])
            label4 = classifier4.classify(train_set[testcv[i]][0])

            a = [label4, label2, label3, label1]
            b = Counter(a)
            y_pred1.append(b)

            a = [label4, label2, label1]
            b = Counter(a)
            y_pred2.append(b)

            a = [label4, label2, label1]
            b = Counter(a)
            y_pred3.append(b)

            a = [label4, label3, label1]
            b = Counter(a)
            y_pred4.append(b)

            a = [label4, label3, label2]
            b = Counter(a)
            y_pred5.append(b)

            a = [label4, label3]
            b = Counter(a)
            y_pred6.append(b)

            a = [label4, label2]
            b = Counter(a)
            y_pred7.append(b)

            a = [label4, label1]
            b = Counter(a)
            #print(b)
            y_pred8.append(b)

        acc1 = metrics.accuracy_score(y_true, y_pred1)
        acc2 = metrics.accuracy_score(y_true, y_pred2)
        acc3 = metrics.accuracy_score(y_true, y_pred3)
        acc4 = metrics.accuracy_score(y_true, y_pred4)
        acc5 = metrics.accuracy_score(y_true, y_pred5)
        acc6 = metrics.accuracy_score(y_true, y_pred6)
        acc7 = metrics.accuracy_score(y_true, y_pred7)
        acc8 = metrics.accuracy_score(y_true, y_pred8)
        sum_accuracy1 += acc1
        sum_accuracy2 += acc2
        sum_accuracy3 += acc3
        sum_accuracy4 += acc4
        sum_accuracy5 += acc5
        sum_accuracy6 += acc6
        sum_accuracy7 += acc7
        sum_accuracy8 += acc8

        k += 1
        # print(str(k) + ')accuracy: ' + str(acc))
        # print('true labels: ' + str(y_true))
        # print('predicted labels: ' + str(y_pred))
        # print('')

    print('ACCURACY 1: ' + str(sum_accuracy1 / k))
    print('ACCURACY 2: ' + str(sum_accuracy2 / k))
    print('ACCURACY 3: ' + str(sum_accuracy3 / k))
    print('ACCURACY 4: ' + str(sum_accuracy4 / k))
    print('ACCURACY 5: ' + str(sum_accuracy5 / k))
    print('ACCURACY 6: ' + str(sum_accuracy6 / k))
    print('ACCURACY 7: ' + str(sum_accuracy7 / k))
    print('ACCURACY 8: ' + str(sum_accuracy8 / k))






    # classifier.train(train_set)
    # return classifier


sentences = []
polar = []
read_file()
train_model(sentences, polar)

