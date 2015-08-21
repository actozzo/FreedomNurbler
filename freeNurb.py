# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 22:46:53 2015

@author: al
Freedom Nurbler

"""
import nltk
import random


okPOS = ['NN', 'NNP', 'NNS'] #allowable nouns of speech
verbs = ['VBD', 'VBP', 'VB', 'VBZ'] #allowable verbs
punc = [',', '.', '!', '?'] #don't nurble punctuation

def nurbWord(taggedWord, verbList):
    if taggedWord[1] in okPOS + punc:
        return taggedWord[0].upper()
    elif taggedWord[1] in verbs:
        return verbList[random.randint(0, len(verbList)-1)].upper()
            # randomly choose verb from list
    return 'nurble'

def untok(words):
    #copied from http://languagelog.ldc.upenn.edu/nll/?p=4282
    return "".join(words[0:1]+ [w if w in punc else " " + w for w in words[1:]])

f = open('sotu2012.txt')
sotu = f.read()
f.close()
sentences = nltk.tokenize.sent_tokenize(sotu)
taggedSentences = [nltk.pos_tag(nltk.word_tokenize(s)) for s in sentences]

v = open('freedomverbs.txt')
verbList = v.read()
verbList = nltk.word_tokenize(verbList)
v.close()

nurbled = open('nurbled.txt', 'w')
nurbled.write("".join(untok([nurbWord(w, verbList) for w in s]) for s in taggedSentences))