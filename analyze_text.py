from text_cleaner import TextCleaner as Cleaner
from collections import Counter, defaultdict
import re
import spacy

text = open('./old_man_and_the_sea.txt').read()

nlp = spacy.load('en')
doc = nlp(text)

def adverb(token):
    return token.pos == spacy.parts_of_speech.ADV

def noun(token):
    return token.pos == spacy.parts_of_speech.NOUN

def adjective(token):
    return token.pos == spacy.parts_of_speech.ADJ

def proper_noun(token):
    return token.pos == spacy.parts_of_speech.PROPN

def verb(token):
    return token.pos == spacy.parts_of_speech.VERB

def unrecognized(token):
    return token.pos == spacy.parts_of_speech.X

def punctuation(token):
    return token.pos == spacy.parts_of_speech.PUNCT

def count_parts_of_speech(doc):
    pos_functions = [adverb, noun, adjective, proper_noun, verb, unrecognized, punctuation]
    counts = {f.__name__:0 for f in pos_functions}

    for token in doc:
        for func in pos_functions:
            if func(token):
                counts[func.__name__]+= 1
    return counts

counts = count_parts_of_speech(doc)
total = len(doc)
print("Total tokens: {:,}".format(total))
for k in sorted(counts, key=counts.get, reverse=True):
    v = counts[k]
    percent = (v/total) * 100
    name = k.replace('_', ' ').title()
    print("{:<15} {:>10,} {:>10.0f}%".format(name, v, percent))

