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

from StringIO import StringIO


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
            c.perform()
            c.close()
            data = buf.getvalue()
            print(word, sentence, data)
            if ("Throttled" in data):
                print("Throttled")
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

        except:
            pass
        # print (good)
        #print (bad)
        shifted = 0
        #if 'not' in sentence:
        #    shifted == 1


    # 0 good
    #1 bad
    #2 neutral
    if ((good > bad) & (shifted == 0)):
        os.system("printf \"0\">> gransent.txt")
        #print ("a good word")
    elif ((good > bad) & (shifted == 1)):
        os.system("printf \"1\">> gransent.txt")
        #print ("bad word")
    elif ((good < bad) & (shifted == 0)):
        os.system("printf \"1\">> gransent.txt")
        # print ("a bad word")
    elif ((good < bad) & (shifted == 1)):
        os.system("printf \"0\">> gransent.txt")
        # print ("good word")
    else:
        os.system("printf \"2\">> gransent.txt")
        # print ("neutral word")


with open("list.txt") as f:
    content = f.readlines()
    for word in content:
        word = word.strip()
        # print(word)
        with open("wordsint4/" + word) as f:
            content = f.readlines()
        sentenceArray = content
        #print(sentenceArray)
        Granularity(sentenceArray)