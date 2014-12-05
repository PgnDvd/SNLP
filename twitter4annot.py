__author__ = 'davide'

import os


def unescape(s):
    if '&' not in s:
        s = re.sub(r'\<.*?\>', '', s)
        s = re.sub(r'\@.*? ', '', s)
        return s
    s = s.replace("&lt;", "<")
    s = s.replace("&#39;", "'")
    s = s.replace("&#10;", ",")
    s = s.replace("&gt;", ">")
    s = s.replace("&apos;", "'")
    s = s.replace("&quot;", '"')
    s = s.replace("&amp;", "&")  # Must be last

    s = re.sub(r'\<.*?\>', '', s)
    s = re.sub(r'\@.*? ', '', s)
    s = re.sub(r'\#.*? ', '', s)
    s = re.sub(r'http.*?&nbsp;', '', s)
    return s


import requests
import re


with open("annot.txt") as f:
    content = f.readlines()
    for word in content:
        print(word)
        link = "https://twitter.com/search?q=" + word + "&src=typd"
        f = requests.get(link)
        text = f.text
        try:
            start = text.index("js-tweet-text tweet-text")
            end = text.index("</p>", start)

            remove1 = 'js-tweet-text tweet-text" lang="en" data-aria-label-part="0">'

            toescape = text[start + len(remove1):end]

            after = re.sub(r'\<.*?\>', '', toescape)
            # print(after)

            data = unescape(after)
            tosearch = word.lower().strip('\n')
            try:
                i = data.lower().index(tosearch)
                print(data)
                toprint = data.encode('ascii', 'ignore')
                toprint = data.strip('\n')
                print(toprint)

                os.system("printf \"" + toprint + "\n\" >> tweet4annot/" + word + ".txt")
            except:
                pass
            # if (tosearch in data.lower()):
            # print(data.lower())

            try:
                while (1):

                    start = text.index("js-tweet-text tweet-text", start + 1)
                    end = text.index("</p>", start)

                    remove1 = 'js-tweet-text tweet-text" lang="en" data-aria-label-part="0">'

                    toescape = text[start + len(remove1):end]

                    after = re.sub(r'\<.*?\>', '', toescape)

                    data = unescape(after)
                    tosearch = word.lower().strip('\n')
                    try:
                        i = data.lower().index(tosearch)
                        toprint = data.encode('ascii', 'ignore')
                        toprint = data.strip('\n')
                        print(toprint)
                        os.system("printf \"" + toprint + "\n\" >> tweet4annot/" + word + ".txt")
                    except:
                        pass
            #finished parsing tweets for the current word
            except:
                print("finish")

        # no tweets for this word
        except Exception as e:
            print(e)






