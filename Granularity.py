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


sentenceArray = ["hello i'm asd beautfil", "asd no ", "asd hey"]


def Granularity(sentenceArray):
    bad = 0
    good = 0
    for sentence in sentenceArray:
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
        print
        json_object['label']
        if str(json_object['label']) == "neg":
            bad = bad + 1
        if str(json_object['label']) == "pos":
            good = good + 1
    print
    good
    print
    bad
    shifted = 0
    if 'not' in sentence shifted = 1
    if good >= bad & shifted = 0:
        print
        "good word"
    if good >= bad & shifted = 1:
        print
        "bad word"
    if good <= bad & shifted = 0:
        print
        "bad word"
    else:
        print
        "good word"


list = []


def getWords(sentence):
    return re.compile('[A-Za-z]+').findall(sentence)


def wordGran(sentenceArray):
    list = []
    good = 0
    bad = 0
    for sentence in sentenceArray:
        list = list + getWords(sentence)
    Granularity(list)


wordGran(sentenceArray)