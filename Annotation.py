__author__ = 'davide'
import os
import random

with open('words.txt') as f:
    content = f.readlines()
    for i in range(1, 2):
        j = random.randint(0, len(content))
        word = content[j].strip()
        os.system("printf \"" + word + "\n\" >> annot.txt")

        try:
            with open('words/' + word + '.txt') as g:
                text = g.readlines()
                # print(text)
            print(content[j].strip(), text)

        except Exception as e:
            print(e)
            i = i - 1
