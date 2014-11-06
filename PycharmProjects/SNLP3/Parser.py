__author__ = 'davide'

import urllib

from HTMLParser import HTMLParser


'''
class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.recording = 0
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag
    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag
    def handle_data(self, data):
        print "Encountered some data  :", data
'''


def word_found(str):
    "This prints a passed string into this function"
    print(str);
    os.system("printf \"" + str + "\n\" >> words.txt")
    # os.popen("curl 'http://www.whatdoestheinternetthink.net/core/client.php?query="+value[17:]+"&searchtype=1' -H 'Host: www.whatdoestheinternetthink.net' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'X-Requested-With: XMLHttpRequest' -H 'Referer: http://www.whatdoestheinternetthink.net/tweet' -H 'Cookie: _ga=GA1.2.655257215.1414603588; _gat=1' -H 'Connection: keep-alive' >> funziona.txt").read()
    os.system(
        "curl 'http://www.whatdoestheinternetthink.net/core/client.php?query=" + str + "&searchtype=1' -H 'Host: www.whatdoestheinternetthink.net' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'X-Requested-With: XMLHttpRequest' -H 'Referer: http://www.whatdoestheinternetthink.net/tweet' -H 'Cookie: _ga=GA1.2.655257215.1414603588; _gat=1' -H 'Connection: keep-alive' >> InternetThink.txt")
    return


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.stampa = 0
        self.data = []

    def handle_starttag(self, tag, attributes):
        if tag != 'a':
            return
        if self.recording:
            self.recording += 1
            return
        for name, value in attributes:
            if name == 'href' and "define.php?term" in value:
                self.stampa = 1
            if "%" in value:
                self.stampa = 0
            if value.count(".") > 1:
                self.stampa = 0
            if "-" in value:
                self.stampa = 0
            if "asd" in value:
                self.stampa = 0
            if "qwe" in value:
                self.stampa = 0
            if "zxc" in value:
                self.stampa = 0
            if "cxz" in value:
                self.stampa = 0
            if "dsa" in value:
                self.stampa = 0
            if "ewq" in value:
                self.stampa = 0
            if len(value) < 22:
                self.stampa = 0
            if len(value) > 50:
                self.stampa = 0
            if value[17:].isupper():
                self.stampa = 0
            if (any(x.isupper() for x in value[18:])):
                self.stampa = 0
            if any(char.isdigit() for char in value):
                self.stampa = 0
            for i in range(0, len(value) - 2):
                if value[i].lower() == value[i + 1].lower() == value[i + 2].lower():
                    self.stampa = 0
            if self.stampa == 1:
                word_found(value[17:]);

        else:
            return
        self.recording = 1

    def handle_endtag(self, tag):
        if tag == 'a' and self.recording:
            self.recording -= 1

    def handle_data(self, data):
        if self.recording:
            self.stampa = 0;


parser = MyHTMLParser()

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', ]
import os


for letter in list:
    for letter2 in list:
        url = "http://www.urbandictionary.com/browse.php?word=" + letter + letter2
        req = urllib.urlopen(url)
        html = str(req.read())  # make it a str object

        # parser.feed(html)
        parser.feed(html)




        # print(html)
        # print(html.find("<div id=\'columnist\'>"))
        # print(html[html.find('<div id=\'columnist\'>\n<ul>\n<li class="popular">'):]) # now you don't need a b in front of your string



