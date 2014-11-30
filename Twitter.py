import os

from TwitterSearch import *

MAXCOUNT = 10
try:

    # Open file word.txt
    # for line in file
    #word = line
    wordgot = 0
    tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
    tso.set_keywords([word])  # let's define all words we would like to have a look for
    tso.set_include_entities(False)  # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key='2sCZOdiLP09Bb1wGnKoiB0jtv',
        consumer_secret='YcrmXG2w6AyNvBS3dEVWzKS5dC7NHzQGMBsQS7AHnaR07ST3mi',
        access_token='244016297-sZcpSDkuk6V9KTy5BGGy5aiOto1J1ekk9aSrcM9R',
        access_token_secret='m4UkHLYktxa1lyzoGUTKxNTHNalAlybjFzTRPxaVHHtQb'
    )

    # this is where the fun actually starts :)
    prova = "ciao"
    for tweet in ts.search_tweets_iterable(tso):
        if (wordgot <= MAXCOUNT)
            if (word in tweet['text'])
                os.system("printf \"" + tweet['text'] + "\n\" >> words/" + word + ".txt")

                print('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ))
                wordgot = wordgot +1

except TwitterSearchException as e:  # take care of all those ugly errors if there are some
    print(e)

