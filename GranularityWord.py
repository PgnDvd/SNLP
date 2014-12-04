'''import pycurl

from StringIO import StringIO


b = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://text-processing.com/api/sentiment/')
c.setopt(pycurl.POSTFIELDS, "text=great")
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.perform()
c.close()
result = b.getvalue()
print(result)
'''

'''import pycurl

from StringIO import StringIO


b = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://text-processing.com/api/sentiment/')
c.setopt(pycurl.POSTFIELDS, "text=great")
c.setopt(pycurl.WRITEFUNCTION, b.write)
c.perform()
c.close()
result = b.getvalue()
print(result)
'''

import json
import pycurl
import os
import re

from StringIO import StringIO


def osprint(param):
    os.system('printf "' + word + ' : ' + str(param) + "\n\">> granword.txt")


def getWords(sentence):
    return re.compile('[A-Za-z]+').findall(sentence)


def wordGran(sentenceArray):
    list = []
    for sentence in sentenceArray:
        list = list + getWords(sentence)
        # print(list)
    Granularity(list)


def Granularity(sentenceArray):
    bad = 0
    good = 0
    for sentence in sentenceArray:
        # print(sentence)
        try:
            buf = StringIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'http://text-processing.com/api/sentiment/')
            c.setopt(c.WRITEFUNCTION, buf.write)
            c.setopt(c.HTTPHEADER, ['Accept-Charset: UTF-8'])
            c.setopt(c.POSTFIELDS, "text=" + sentence)
            c.setopt(pycurl.PROXY, '127.0.0.1:9050')
            c.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
            c.perform()
            c.close()
            data = buf.getvalue()
            os.system("printf \"" + word + " , " + sentence + data + "\n\">> granworddebug.txt")
            print(word, sentence, data)
            if ("Throttled" in data):
                print("Throttled")
                from TorCtl import TorCtl

                conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9151, passphrase="zazaking")
                print(conn.is_live())
                conn.send_signal("NEWNYM")
                # conn.sendAndRecv('signal newnymrn')
                conn.close()
                import time

                time.sleep(5)
                print
                "renewed"
            info = json.dumps(data)
            json_object = json.loads(json.loads(info))
            # print(json_object)
            #print(json_object['label'])
            if str(json_object['label']) == "neg":
                #print("neg")
                bad = bad + 1
            if str(json_object['label']) == "pos":
                #print("pos")
                good = good + 1

        except Exception as e:
            print(e)
        # print (good)
        # print (bad)
        shifted = 0
        #if 'not' in sentence:
        #    shifted == 1


    # 0 good
    # 1 bad
    #2 neutral
    if ((good > bad) & (shifted == 0)):
        osprint(0)
        #print ("a good word")
    elif ((good > bad) & (shifted == 1)):
        osprint(1)
        #print ("bad word")
    elif ((good < bad) & (shifted == 0)):
        osprint(1)
        # print ("a bad word")
    elif ((good < bad) & (shifted == 1)):
        osprint(0)
        # print ("good word")
    else:
        osprint(2)
        # print ("neutral word")


with open("list.txt") as f:
    content = f.readlines()
    for word in content:
        word = word.strip()
        # print(word)
        with open("wordsint4/" + word) as f:
            content = f.readlines()
        sentenceArray = content
        # print(sentenceArray)
        wordGran(sentenceArray)