__author__ = 'davide'

import urllib

import os


def sentence_tag(sentence, word):
    # print(sentence)
    # print(word)
    import nltk

    text = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(text)
    # print tagged
    # for t in tagged:
    #print t[0]
    for t in tagged:
        if t[0].lower() == word.lower():
            #print(t[0].lower())
            #print(word.lower())
            os.system("printf \"" + t[0].lower() + ": " + t[1] + "\n\" >> wordstoken.txt")

            os.system("printf \"" + sentence + "\n\" >> words/" + word + ".txt")
            #print("-------------------------------------")


from BeautifulSoup import BeautifulSoup

j = 0
previous_word = "aarori"
with open("words.txt") as f:
    for line in f:

        url = "http://www.urbandictionary.com/define.php?term=" + line
        page = urllib.urlopen(url).read()
        # soup = BeautifulSoup(page)
        soup = BeautifulSoup(page.decode('utf-8', 'ignore'))

        soup.prettify()
        i = 0
        if (j != 0):
            print
            text;

            # passare =text.decode('utf-8').strip()
            passare = "".join([ch for ch in text if ord(ch) < 128])
            # passare = text.encode('ascii','ignore')
            passare2 = "".join([ch for ch in previous_word if ord(ch) < 128])
            #passare2 =previous_word.strip()
            sentence_tag(passare.strip(), passare2.strip())
            #print(url)
            previous_word = line

        text = ""
        j = 1
        for anchor in soup.find("div", {"class": "example"}):
            # print (i)
            if i == 0:
                text = str(anchor).replace("<br />", " ")
            else:
                text += str(anchor).replace("<br />", " ")
            i = i + 1;
            # print text
            text = text.replace("&amp;", "&")
            text = text.replace("&quot;", '"')
            text = text.replace("&apos;", "'")
            text = text.replace("&gt;", ">")
            text = text.replace("&l;", "<")

            # print text






































            # from HTMLParser import HTMLParser
            # parser = HTMLParser()
            # text = text.encode('utf-8', 'ignore')
            #
            # text = text.decode('utf-8')
            #
            #text = parser.unescape(text)
            #print text






            #for anchor in soup.findAll('div'):
            #    print anchor['class'];
'''
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
'''

#
#
#
# class MyHTMLParser(HTMLParser):
# def __init__(self):
# HTMLParser.__init__(self)
#         self.inLink = False
#         self.dataArray = []
#         self.countLanguages = 0
#         self.lasttag = None
#         self.lastname = None
#         self.lastvalue = None
#
#     def handle_starttag(self, tag, attrs):
#         self.inLink = False
#         if tag == 'div':
#             for name, value in attrs:
#                 if name == 'class' and value == 'example':
#                     self.countLanguages += 1
#                     self.inLink = True
#                     self.lasttag = tag
#                     print("miao")
#
#     def handle_endtag(self, tag):
#         if tag == "div":
#             self.inlink = False
#
#     def handle_data(self, data):
#         if self.lasttag == 'div' and self.inLink and data.strip():
#             text = html_decoded_string = parser.unescape(data)
#             content = text.decode('utf-8')
#             print(content.rstrip())
#             print("end")
#             sentence_tag(content.rstrip())
