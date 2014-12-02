__author__ = 'davide'
import os

with open("internetnewline.txt") as f:
    content = f.readlines()
    for word in content:
        success = "success\":1"
        if (success in word):
            print(word)
            i = word.index("search\"")
            j = word.index("winner")
            print(i)
            print(j)
            parola = word[i + 9:j - 3]
            print(parola)
            os.system("printf \"" + parola + "\n\" >> intwords.txt")

