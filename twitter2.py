__author__ = 'davide'
import time
import os

from TwitterSearch import *


MAXCOUNT = 10

tso = TwitterSearchOrder()  # create a TwitterSearchOrder object


# it's about time to create a TwitterSearch object with our secret tokens

ts2 = TwitterSearch(
    consumer_key='2sCZOdiLP09Bb1wGnKoiB0jtv',
    consumer_secret='YcrmXG2w6AyNvBS3dEVWzKS5dC7NHzQGMBsQS7AHnaR07ST3mi',
    access_token='244016297-sZcpSDkuk6V9KTy5BGGy5aiOto1J1ekk9aSrcM9R',
    access_token_secret='m4UkHLYktxa1lyzoGUTKxNTHNalAlybjFzTRPxaVHHtQb'
)

ts1 = TwitterSearch(
    consumer_key='nVTulrdo7EeODLssb2wqYu4t8',
    consumer_secret='mwSgwIxuFKJfGOUs6zMhZrpYa82UtXrIO7GKe4rTyFVtk7Jvzy',
    access_token='244016297-Yl146wuXUzWLjnLLudFSaMTAsTtYv9OwydpN20as',
    access_token_secret='LCwPyBPqdJpABnJLYITmMK9BcS7kiCdMKpVF8N4271hM4'
)


def fib(word):
    tso.set_keywords([word])  # let's define all words we would like to have a look for
    tso.set_include_entities(False)  # and don't give us all those entity information
    # this is where the fun actually starts :)
    wordgot = 0

    for tweet in ts.search_tweets_iterable(tso):
        if (wordgot <= MAXCOUNT):
            wordstring = " " + word + " "
            if (wordstring in tweet['text']):
                print(tweet)

                print('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ))
                toprint = tweet['text'].encode('ascii', 'ignore').strip('\n')
                os.system("printf \"" + toprint + "\n\" >> words2/" + word + ".txt")

                wordgot = wordgot + 1


start_time2 = time.time()
start_time1 = 0

switch = 0
ts = ts2
with open("words.txt") as f:
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
            if ((elapsed_time1 < 900) & (elapsed_time2 < 900)):
                print("sleeping")

                time.sleep(910 - elapsed_time1)
                ts = ts1
                switch = 0
                start_time1 = time.time()
            elif (elapsed_time1 < 900):
                print("switch to 2")
                ts = ts2
                switch = 1
                start_time2 = time.time()
            elif (elapsed_time2 < 900):
                print("switch to 1")
                ts = ts1
                switch = 0
                start_time1 = time.time()
            fib(word)

