# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 22:46:53 2015

@author: al
Freedom Nurbler

"""
import nltk


okPOS = ['NN', 'NNP', 'NNS'] #allowable nouns of speech
verbs = ['VBD', 'VBP', 'VB', 'VBZ'] #allowable verbs
punc = [',', '.', '!', '?'] #don't nurble punctuation

def nurbWord(taggedWord):
    if taggedWord[1] in okPOS + punc:
        return taggedWord[0].upper()
    elif taggedWord[1] in verbs:
        if rand() <= 0.1:
            # randomly choose verb from list
            return
    return 'nurble'

f = open('sotu2012.txt')
sotu = f.read()
f.close()
sentences = nltk.tokenize(sotu)
taggedSentences = [nltk.pos_tag(nltk.word_tokenize(s)) for s in sentences]

v = open('freedomverbs.txt')
verbList = v.read()
v.close()