__author__ = 'davide'

import urllib

from HTMLParser import HTMLParser


def sentence_tag(str):
    print(str)
    import nltk
    text = nltk.word_tokenize(str)
    tagged = nltk.pos_tag(text)
    print(tagged)



class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.inLink = False
        self.dataArray = []
        self.countLanguages = 0
        self.lasttag = None
        self.lastname = None
        self.lastvalue = None

    def handle_starttag(self, tag, attrs):
        self.inLink = False
        if tag == 'div':
            for name, value in attrs:
                if name == 'class' and value == 'example':
                    self.countLanguages += 1
                    self.inLink = True
                    self.lasttag = tag
                    print("miao")

    def handle_endtag(self, tag):
        if tag == "div":
            self.inlink = False

    def handle_data(self, data):
        if self.lasttag == 'div' and self.inLink and data.strip():
            text = html_decoded_string = parser.unescape(data)
            content = text.decode('utf-8')
            print(content.rstrip())
            print("end")
            sentence_tag(content.rstrip())



with open("words.txt") as f:
    for line in f:
        url = "http://www.urbandictionary.com/define.php?term=" + line
        print(url)
        req = urllib.urlopen(url)
        html = str(req.read())  # make it a str object
        print("aaaaaa")
        # print(html)
        html = html.replace("<br>", " ")
        html = html.replace("<br/>", " ")
        print("bbbb")
        #print (html)
        parser = MyHTMLParser()
        # parser.feed(html)
        print("ciao")
        parser.feed(html)




sentenceArray = "hello i'm beautfil", "asd ", "asd"
word_polarize(sentenceArray)
sentence_polarize(sentenceArray)
