#This code imports the necessary modules.

import os
import random
import datetime

right_now = datetime.datetime.now().isoformat()          
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

tim = ("".join(list))

srchstr = 'C:\\Users\\mysti\\thomasoriginalcode\\Git\\PhraseGenerator\\'

content =[]

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".txt"): 
            astr = str(file)
            content.append(astr)

texcon = []

for elem in content:

    infile = open(elem, "r")

    aline = infile.readline()
    while aline:
        try:
            texcon.append(aline)
            aline = infile.readline()
        except: print("Text error-- passing over line.")

    infile.close()

wordcon = []

for elem in texcon:
    al = elem.split()
    for x in al:
        addstr = ""
        for xlet in x:
            if xlet.isalnum():
                addstr += xlet
        xl = addstr.strip()
        xl2 = xl.lower()
        if len(xl2) > 1:
            wordcon.append(xl2)
            
x1 = len(wordcon)

phraselist = []

for phrs in range(25):

    for wiz in range(3):
        num1 = random.randrange(x1)
        num2 = random.randrange(x1)
        num3 = random.randrange(x1)
        astr = wordcon[num1]
        bstr = wordcon[num2]
        cstr = wordcon[num3]
        phrsstr = astr + " " + bstr + " " + cstr
        phraselist.append(phrsstr)

outp = "GeneratedPhrases" + tim + ".txt"

outfile = open(outp, "w")

outfile.write("Here are random phrases, assembled from any .txt files in the code's root folder:" + '\n')
outfile.write("There are a total of 25 phrases included in this list." + '\n')
outfile.write('\n')

for elem in phraselist:

    astr = elem + '\n'
    outfile.write(astr)

outfile.close()

print("")
print("Your phrase list has been created, and that document can be found in the same folder as this code. Thank you.")
print("")

## THE GHOST OF THE SHADOW ##
