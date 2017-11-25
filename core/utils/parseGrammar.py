from os import listdir
from pprint import pprint

rules = {}
files = [x for x in listdir("../rules") if '~' not in x]
for fileName in files:
    with open ("../rules/"+fileName) as f:
        if fileName not in rules:
            rules[fileName] = {}
        for line in f.readlines():
            line = line.strip("\n")
            rightNote = line.split(":")[0]
            leftChord = line.split(":")[1].split(" ")
            if rightNote not in rules[fileName]:
                rules[fileName][rightNote] = []
            rules[fileName][rightNote].append(leftChord)
pprint(rules)
