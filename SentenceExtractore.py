__author__ = 'davide'

import urllib

from HTMLParser import HTMLParser


def sentence_tag(str):
    tokens = ntlk.word_tokenize(str);
    return


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

    def handle_endtag(self, tag):
        if tag == "div":
            self.inlink = False

    def handle_data(self, data):
        if self.lasttag == 'div' and self.inLink and data.strip():
            sentence_tag(data)


print(
    "19 of the UDHR.<br/><br/>This is used when someone claims your opinion is wrong or incorrect. If someone has this brought up, they have been Aarowned.</div>")
with open("words.txt") as f:
    for line in f:
        url = "http://www.urbandictionary.com/define.php?term=" + line
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
        parser.feed(html)


