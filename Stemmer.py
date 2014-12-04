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

import os
import re

from nltk.stem.snowball import EnglishStemmer


def osprint(param):
    os.system('printf "' + word + ' : ' + str(param) + "\n\">> gransent.txt")


def Granularity(sentenceArray):
    for sentence in sentenceArray:
        # print(sentence)
        try:

            stemmer = EnglishStemmer()
            sentence = re.sub(r'\#.*?$', '', sentence)
            sentence = re.sub(r'\#.*? ', '', sentence)
            sentence = re.sub(r'\@.*?$', '', sentence)
            sentence = re.sub(r'\@.*? ', '', sentence)
            sentence = re.sub(r'pic.twitter.*?$', '', sentence)
            sentence = re.sub(r'pic.twitter.*? ', '', sentence)
            sentence = re.sub(r'\'m', ' am', sentence)
            sentence = re.sub(r'\'d', ' would', sentence)
            sentence = re.sub(r'\'ll', ' will', sentence)
            sentence = re.sub(r'\&', 'and', sentence)
            sentence = re.sub(r'don\'t', 'do not', sentence)

            data = stemmer.stem(sentence)
            print(data)
            from nltk.corpus import stopwords

            sentence = str(data)
            stop = stopwords.words('english')
            final = [i for i in sentence.split() if i not in stop]
            finalstring = ' '.join(final)
            os.system("printf \"" + str(finalstring) + "\n\">> stemstop/" + word)
        except Exception as e:
            print(e)


'''
            buf = StringIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'http://text-processing.com/api/stem/')
            c.setopt(c.WRITEFUNCTION, buf.write)
            c.setopt(c.HTTPHEADER, ['Accept-Charset: UTF-8'])
            c.setopt(c.POSTFIELDS, "text=" + sentence)
            c.setopt(pycurl.PROXY, '127.0.0.1:9050')
            c.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5)
            c.perform()
            c.close()
            data = buf.getvalue()
            os.system("printf \""+word+" , "+sentence+data+"\n\">> gransentdebug.txt")
            print(word, sentence, data)
            if ("Throttled" in data):
                print("Throttled")
                from TorCtl import TorCtl
                conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9151, passphrase="zazaking")
                print(conn.is_live())
                conn.send_signal("NEWNYM")
                #conn.sendAndRecv('signal newnymrn')
                conn.close()
                import time
                time.sleep(5)
                print "renewed"
'''

with open("list.txt") as f:
    content = f.readlines()
    for word in content:
        word = word.strip()
        # print(word)
        with open("wordsint4/" + word) as f:
            content = f.readlines()
        sentenceArray = content
        # print(sentenceArray)
        Granularity(sentenceArray)