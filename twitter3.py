__author__ = 'davide'
import time
import os

from TwitterSearch import *


MAXCOUNT = 10

tso = TwitterSearchOrder()  # create a TwitterSearchOrder object


# it's about time to create a TwitterSearch object with our secret tokens

ts = TwitterSearch(
    consumer_key='QxO3pRPC5P0DsE220jBg',
    consumer_secret='8UlorkGHQvLi6yh9nOEc9m1361hkqWDlA3VlYDB8nA',
    access_token='52757477-UU9bjbrTIkV336j6SdP87bVAfM6ffN7bWJ5XIir1K',
    access_token_secret='yWzFcCHR9lxXgYkyI05rSB7QI8j7jKbxjfQbZN4jg'
)

ts1 = TwitterSearch(
    consumer_key='khH1Bs4prVt0MZCdiZje6qvOZ',
    consumer_secret='6IM8wR7cepU6oh2zDpnMH1bURVejdYoRTKzv73txydUEeG1Wo1',
    access_token='244016297-XvYTVFtmcOknibJgSnLVZ77kTA6CZ9LtZ6AYEAhG',
    access_token_secret='b6dAEYmdSGqX219YeN0io382ZqU6g5vMYaNbILjH3535B'
)

ts2 = TwitterSearch(
    consumer_key='RVHpuqpjJyxbdPCVqTyYikwF6',
    consumer_secret='skzWw46b8DdLa0tLmEugll9WzO7g2s2O4wEEps7R72kZd4Z6ZX',
    access_token='244016297-qX3W8F3mWp5hRgztBrl64g1uq8HXeuI2yC3SydFb',
    access_token_secret='kqEAvAi2hlPxr05jBKgbOSxBa58qc9Wu2mwcKMENapmxd'
)


def fib(word):
    tso.set_keywords([word])  # let's define all words we would like to have a look for
    tso.set_include_entities(False)  # and don't give us all those entity information
    tso.set_language('en')
    # this is where the fun actually starts :)
    wordgot = 0

    for tweet in ts.search_tweets_iterable(tso):
        if (wordgot <= MAXCOUNT):
            wordstring = " " + word + " "
            if (wordstring in tweet['text']):
                print(tweet)

                print('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ))
                toprint = tweet['text'].encode('ascii', 'ignore')
                toprint = toprint.strip('\n')
                os.system("printf \"" + toprint + "\n\" >> wordsint2/" + word + ".txt")

                wordgot = wordgot + 1


start_time1 = time.time()
start_time2 = 0

switch = 0
ts = ts1
with open("intwords.txt") as f:
    content = f.readlines()
    for word in content:
        word = word.strip('\n')
        print(word)
        try:
            fib(word)

        except Exception as e:  # take care of all those ugly errors if there are some
            print(e)
            print("Ciao")
            elapsed_time1 = time.time() - start_time1
            elapsed_time2 = time.time() - start_time2
            '''
            if((elapsed_time1< 900) & (elapsed_time2 < 900)):
                print("sleeping")

                time.sleep(910)
                ts = ts1
                switch = 0
                start_time1 = time.time()
            elif(elapsed_time1 < 900):
                    print("switch to 2")
                    ts = ts2
                    switch = 1
                    start_time2 = time.time()
            elif (elapsed_time2 < 900):
                    print("switch to 1")
                    ts = ts1
                    switch = 0
                    start_time1 = time.time()
            '''
            if (switch == 0):
                print("switch to 2")
                ts = ts2
                switch = 1
                start_time2 = time.time()
            elif (switch == 1):
                k = 0
                while (k < 910 - elapsed_time1):
                    print("sleeping" + str(k))

                    time.sleep(100)
                    k += 100

                print("switch to 1")
                ts = ts1
                switch = 0
                start_time1 = time.time()

            fib(word)

