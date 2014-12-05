from collections import defaultdict
from os.path import expanduser
import csv

import nltk
from sklearn import cross_validation
from sklearn import naive_bayes
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from scipy import stats
from sklearn.tree import DecisionTreeClassifier


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
                # 0 good
                #1 bad
                #2 neutral

                sentences.append(row[0])
                if ('neg' in row[1]):
                    polar.append(1)
                if ('pos' in row[1]):
                    polar.append(0)
                if ('ind' in row[1]):
                    polar.append(2)
            except Exception as e:
                print(e)
                if ('neg' in row[0]):
                    polar.append(1)
                if ('pos' in row[0]):
                    polar.append(0)
                if ('ind' in row[0]):
                    polar.append(2)


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
    sum_anova = 0
    k = 0
    for traincv, testcv in cv:

        classifier1 = nltk.SklearnClassifier(naive_bayes.MultinomialNB()).train(
            train_set[traincv[0]:traincv[len(traincv) - 1]])
        classifier2 = nltk.MaxentClassifier.train(train_set[traincv[0]:traincv[len(traincv) - 1]], max_iter=10)
        classifier3 = nltk.SklearnClassifier(LogisticRegression()).train(
            train_set[traincv[0]:traincv[len(traincv) - 1]])
        classifier4 = nltk.SklearnClassifier(LinearSVC()).train(train_set[traincv[0]:traincv[len(traincv) - 1]])
        classifier5 = nltk.SklearnClassifier(DecisionTreeClassifier()).train(
            train_set[traincv[0]:traincv[len(traincv) - 1]])

        y_true1 = []
        y_pred1 = []
        y_true2 = []
        y_pred2 = []
        y_true3 = []
        y_pred3 = []
        y_true4 = []
        y_pred4 = []
        y_true5 = []
        y_pred5 = []
        for i in range(len(testcv)):
            y_true1.append(train_set[testcv[i]][1])
            y_pred1.append(classifier1.classify(train_set[testcv[i]][0]))
            # if("saumya" in str(train_set[testcv[i]][0])):

            #else:
            #y_pred1.append(classifier1.classify(train_set[testcv[i]][0]))
        print(y_pred1)
        for i in range(len(testcv)):
            y_true2.append(train_set[testcv[i]][1])
            y_pred2.append(classifier2.classify(train_set[testcv[i]][0]))
        for i in range(len(testcv)):
            y_true3.append(train_set[testcv[i]][1])
            y_pred3.append(classifier3.classify(train_set[testcv[i]][0]))
        for i in range(len(testcv)):
            y_true4.append(train_set[testcv[i]][1])
            y_pred4.append(classifier4.classify(train_set[testcv[i]][0]))
        for i in range(len(testcv)):
            y_true5.append(train_set[testcv[i]][1])
            y_pred5.append(classifier5.classify(train_set[testcv[i]][0]))

        f_val, p_val = stats.f_oneway(y_pred1, y_pred2, y_pred3, y_pred4, y_pred5)

        print("One-way ANOVA P =", p_val)

        f_val, p_val12 = stats.f_oneway(y_pred1, y_pred2)
        f_val, p_val13 = stats.f_oneway(y_pred1, y_pred3)
        f_val, p_val14 = stats.f_oneway(y_pred1, y_pred4)
        f_val, p_val23 = stats.f_oneway(y_pred3, y_pred2)
        f_val, p_val24 = stats.f_oneway(y_pred4, y_pred2)
        f_val, p_val34 = stats.f_oneway(y_pred3, y_pred4)

        f_val, p_val15 = stats.f_oneway(y_pred5, y_pred1)
        f_val, p_val25 = stats.f_oneway(y_pred5, y_pred2)
        f_val, p_val35 = stats.f_oneway(y_pred5, y_pred3)
        f_val, p_val54 = stats.f_oneway(y_pred5, y_pred4)

        print(p_val12, p_val13, p_val14, p_val23, p_val24, p_val34, p_val15, p_val25, p_val35, p_val54)
        sum_anova += p_val

        k += 1
        print(str(k) + ')anova: ' + str(p_val))

    print('ANOVA: ' + str(sum_anova / k))


'''
count_vect = CountVectorizer(encoding='latin-1')
train_fitted = count_vect.fit_transform(train)
arr1 = numpy.full((139),1)
arr2 = numpy.full((20),0)
train_target = numpy.concatenate((arr1, arr2))
# type(train_target): <type 'numpy.ndarray'>
# train_target
# array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
#   1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
test_transform = count_vect.transform(test)
anova = SelectKBest(f_classif, k=selectk)
train_anova = anova.fit_transform(train_fitted, train_target) #
'''

# classifier.train(train_set)#aggiungere max_iter per maxent
#return classifier


sentences = []
polar = []
read_file()
# train_model(sentences, polar)

