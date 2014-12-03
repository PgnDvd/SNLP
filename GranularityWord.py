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
import re

from StringIO import StringIO


sentenceArray = ["hello i'm good beautfil", "reddit sucks ", "i'm wonderfully hungry"]
print(sentenceArray)


def Granularity(sentenceArray):
    bad = 0
    good = 0
    for sentence in sentenceArray:
        # print(sentence)
        buf = StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, 'http://text-processing.com/api/sentiment/')
        c.setopt(c.WRITEFUNCTION, buf.write)
        c.setopt(c.HTTPHEADER, ['Accept-Charset: UTF-8'])
        c.setopt(c.POSTFIELDS, "text=" + sentence)
        c.perform()
        c.close()
        data = buf.getvalue()
        info = json.dumps(data)
        json_object = json.loads(json.loads(info))
        #print(json_object)
        #print(json_object['label'])
        if str(json_object['label']) == "neg":
            #print("neg")
            bad = bad + 1
        if str(json_object['label']) == "pos":
            #print("pos")
            good = good + 1
    # print (good)
    #print (bad)
    shifted = 0
    #if 'not' in sentence:
    #    shifted == 1
    if ((good > bad) & (shifted == 0)):
        print("a good word")
    elif ((good > bad) & (shifted == 1)):
        print("bad word")
    elif ((good < bad) & (shifted == 0)):
        print("a bad word")
    elif ((good < bad) & (shifted == 1)):
        print("good word")
    else:
        print("neutral word")


def getWords(sentence):
    return re.compile('[A-Za-z]+').findall(sentence)


def wordGran(sentenceArray):
    list = []
    for sentence in sentenceArray:
        list = list + getWords(sentence)
        # print(list)
    Granularity(list)


wordGran(sentenceArray)
Granularity(sentenceArray)