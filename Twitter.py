from TwitterSearch import *

MAXCOUNT = 10

try:
    # Open file word.txt
    # for line in file
    #word = line
    with open("words.txt") as f:
        content = f.readlines()
        for word in content:
            word = word.strip('\n')
            print(word)
            wordgot = 0
            #
            # import subprocess
            # print 'sending command: '
            # command = "'https://api.twitter.com/1.1/application/rate_limit_status.json' --data 'resources=search' --header 'Authorization: OAuth oauth_consumer_key=\"2sCZOdiLP09Bb1wGnKoiB0jtv\", oauth_nonce=\"6ac6c4bddc0cf624d9285d0dab13d61d\", oauth_signature=\"63svXKmvlc%2BqlK5WxB8dBuTbn3Y%3D\", oauth_signature_method=\"HMAC-SHA1\", oauth_timestamp=\"1417461273\", oauth_token=\"244016297-sZcpSDkuk6V9KTy5BGGy5aiOto1J1ekk9aSrcM9R\", oauth_version=\"1.0\"' --verbose"
            # q = subprocess.check_output(["curl","--get",command])
            # print (q)
            # p = subprocess.check_output(command, stdout=subprocess.PIPE).communicate()[0]
            # print(p)
            # print( subprocess.check_output('curl','--get','https://api.twitter.com/1.1/application/rate_limit_status.json','--data','resources=search','--header','Authorization: OAuth,oauth_consumer_key="2sCZOdiLP09Bb1wGnKoiB0jtv" oauth_nonce="6ac6c4bddc0cf624d9285d0dab13d61d"  oauth_signature="63svXKmvlc%2BqlK5WxB8dBuTbn3Y%3D"  oauth_signature_method="HMAC-SHA1"  oauth_timestamp="1417461273"  oauth_token="244016297-sZcpSDkuk6V9KTy5BGGy5aiOto1J1ekk9aSrcM9R"  oauth_version="1.0"','--verbose',))

            import json
            import pycurl

            from StringIO import StringIO
            import os


            # -------------------------------------------------------------------
            #-------------------------------------------------------------------
            #-------------------------------------------------------------------

            #-------------------------------------------------------------------
            #MODIFY THIS
            command = "curl --get 'https://api.twitter.com/1.1/application/rate_limit_status.json' --data 'resources=search' --header 'Authorization: OAuth oauth_consumer_key=\"2sCZOdiLP09Bb1wGnKoiB0jtv\", oauth_nonce=\"6ac6c4bddc0cf624d9285d0dab13d61d\", oauth_signature=\"63svXKmvlc%2BqlK5WxB8dBuTbn3Y%3D\", oauth_signature_method=\"HMAC-SHA1\", oauth_timestamp=\"1417461273\", oauth_token=\"244016297-sZcpSDkuk6V9KTy5BGGy5aiOto1J1ekk9aSrcM9R\", oauth_version=\"1.0\"' --verbose"
            # -------------------------------------------------------------------
            #-------------------------------------------------------------------
            #-------------------------------------------------------------------
            #-------------------------------------------------------------------


            '''
            r = os.popen(command).read()
            import json
            from pprint import pprint
            import time

            data = json.loads(r)
            print(r)
            print(data['resources']['search']['/search/tweets']['limit'])
            print(data['resources']['search']['/search/tweets']['remaining'])
            print(data['resources']['search']['/search/tweets']['reset'])
            if (data['resources']['search']['/search/tweets']['remaining'] < 10):
                time.sleep(data['resources']['search']['/search/tweets']['reset'])


            '''
            #
            # buf = StringIO()
            # c = pycurl.Curl()
            # c.setopt(c.URL, 'https://api.twitter.com/1.1/application/rate_limit_status.json')
            # c.setopt(c.WRITEFUNCTION, buf.write)
            # c.setopt(c.HTTPHEADER, ["Authorization: OAuth oauth_consumer_key=\"2sCZOdiLP09Bb1wGnKoiB0jtv\"",
            #                         "oauth_nonce=\"6ac6c4bddc0cf624d9285d0dab13d61d\"",
            #                         "oauth_signature=\"63svXKmvlc%2BqlK5WxB8dBuTbn3Y%3D\"",
            #                         "oauth_signature_method=\"HMAC-SHA1\"",
            #                         "oauth_timestamp=\"1417461273\"",
            #                         "oauth_token=\"244016297-sZcpSDkuk6V9KTy5BGGy5aiOto1J1ekk9aSrcM9R\"",
            #                         "oauth_version=\"1.0\""])
            # c.setopt(c.POSTFIELDS, "resources=search")
            # c.perform()
            # c.close()
            # data = buf.getvalue()
            # print(data)
            # info = json.dumps(data)
            # json_object = json.loads(json.loads(info))
            # print(json_object)
            # print("hi")


            tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
            tso.set_keywords([word])  # let's define all words we would like to have a look for
            tso.set_include_entities(False)  # and don't give us all those entity information
            # -------------------------------------------------------------------
            #-------------------------------------------------------------------
            #-------------------------------------------------------------------
            #-------------------------------------------------------------------
            #-------------------------------------------------------------------
            #-------------------------------------------------------------------
            #-------------------------------------------------------------------
            #-------------------------------------------------------------------
            #MODIFY THIS

            # it's about time to create a TwitterSearch object with our secret tokens
            ts = TwitterSearch(
                consumer_key='2sCZOdiLP09Bb1wGnKoiB0jtv',
                consumer_secret='YcrmXG2w6AyNvBS3dEVWzKS5dC7NHzQGMBsQS7AHnaR07ST3mi',
                access_token='244016297-sZcpSDkuk6V9KTy5BGGy5aiOto1J1ekk9aSrcM9R',
                access_token_secret='m4UkHLYktxa1lyzoGUTKxNTHNalAlybjFzTRPxaVHHtQb'
            )






            # this is where the fun actually starts :)
            for tweet in ts.search_tweets(tso):
                print(tweet)
                if (wordgot <= MAXCOUNT):
                    wordstring = " " + word + " "
                    if (wordstring in tweet['text']):
                        print('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ))

                        #os.system("printf \"" + tweet['text'] + "\n\" >> words/" + word + ".txt")

                        wordgot = wordgot + 1

except TwitterSearchException as e:  # take care of all those ugly errors if there are some
    print(e)

    # print(e)
    # import json
    # import pycurl
    #
    # from StringIO import StringIO
    #
    # buf = StringIO()
    # c = pycurl.Curl()
    # c.setopt(c.URL, 'https://api.twitter.com/1.1/application/rate_limit_status.json')
    # c.setopt(c.WRITEFUNCTION, buf.write)
    # c.setopt(c.HTTPHEADER, ['Accept-Charset: UTF-8'])
    # c.setopt(c.POSTFIELDS,
    # "--data \'resources=search\' --header \'Authorization: OAuth oauth_consumer_key=\"2sCZOdiLP09Bb1wGnKoiB0jtv\", oauth_nonce=\"6ac6c4bddc0cf624d9285d0dab13d61d\", oauth_signature=\"63svXKmvlc%2BqlK5WxB8dBuTbn3Y%3D\", oauth_signature_method=\"HMAC-SHA1\", oauth_timestamp=\"1417461273\", oauth_token=\"244016297-sZcpSDkuk6V9KTy5BGGy5aiOto1J1ekk9aSrcM9R\", oauth_version=\"1.0\"\' --verbose")
    # c.perform()
    # c.close()
    # data = buf.getvalue()
    # info = json.dumps(data)
    # json_object = json.loads(json.loads(info))
    #

    # import subprocess
    #
    # proc = subprocess.Popen(["curl", "--get", "https://api.twitter.com/1.1/application/rate_limit_status.json",
    # "--data", "resources=search",
    #                          "--header", "Authorization: OAuth oauth_consumer_key=\"2sCZOdiLP09Bb1wGnKoiB0jtv\", oauth_nonce=\"6ac6c4bddc0cf624d9285d0dab13d61d\", oauth_signature=\"63svXKmvlc%2BqlK5WxB8dBuTbn3Y%3D\", oauth_signature_method=\"HMAC-SHA1\", oauth_timestamp=\"1417461273\", oauth_token=\"244016297-sZcpSDkuk6V9KTy5BGGy5aiOto1J1ekk9aSrcM9R\", oauth_version=\"1.0\"'",
    #                          "--verbose"], stdout=buf)
    # (out, err) = proc.communicate()
    # print out
    # print err
    # data = buf.getvalue()
    # print(data)
    # print("hey")
    # print(e)


    # outfile=''  #put your file path there
    # os.system("curl --get \'https://api.twitter.com/1.1/application/rate_limit_status.json\' --data \'resources=search\' --header \'Authorization: OAuth oauth_consumer_key=\"2sCZOdiLP09Bb1wGnKoiB0jtv\", oauth_nonce=\"6ac6c4bddc0cf624d9285d0dab13d61d\", oauth_signature=\"63svXKmvlc%2BqlK5WxB8dBuTbn3Y%3D\", oauth_signature_method=\"HMAC-SHA1\", oauth_timestamp=\"1417461273\", oauth_token=\"244016297-sZcpSDkuk6V9KTy5BGGy5aiOto1J1ekk9aSrcM9R\", oauth_version=\"1.0\"\' --verbose".format(x=str(outfile))  #Outputs command to log file (and creates it if it doesnt exist).
    # readOut=open("{z}".format(z=str(outfile),"r")  #Opens file in reading mode.
    # for line in readOut:
    #     print line  #Prints lines in file
    # readOut.close()  #Closes file
    # os.system("del {c}".format(c=str(outfile))  #This is optional, as it just deletes the log file after use.

