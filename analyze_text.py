import spacy

class TextAnalyzer:

  @staticmethod
  def analyze(text):
    nlp = spacy.load('en')
    doc = nlp(text)
    counts = TextAnalyzer.count_parts_of_speech(doc)
    total = len(doc)
    print("Total tokens: {:,}".format(total))
    for k in sorted(counts, key=counts.get, reverse=True):
      count = counts[k]
      percent = (count/total) * 100
      name = k.replace('_', ' ').title()

    print("{:<20} {:>10,} {:>10.0f}%".format(name, count, percent))

  @staticmethod
  def count_parts_of_speech(doc):
    parts_of_speech = {
      "Adverb": [spacy.parts_of_speech.ADV],
      "Adjective": [spacy.parts_of_speech.ADJ],
      "Adposition": [spacy.parts_of_speech.ADP],
      "Auxiliary": [spacy.parts_of_speech.AUX],
      "Conjunction": [spacy.parts_of_speech.CONJ, spacy.parts_of_speech.CCONJ, spacy.parts_of_speech.SCONJ],
      "Determiner": [spacy.parts_of_speech.DET],
      "Interjection": [spacy.parts_of_speech.INTJ],
      "Noun": [spacy.parts_of_speech.NOUN],
      "Numeral": [spacy.parts_of_speech.NUM],
      "Particle": [spacy.parts_of_speech.PART],
      "Pronoun": [spacy.parts_of_speech.PRON],
      "Proper Noun": [spacy.parts_of_speech.PROPN],
      "Punctuation & Spaces": [spacy.parts_of_speech.PUNCT, spacy.parts_of_speech.SYM, spacy.parts_of_speech.SPACE],
      "Verb": [spacy.parts_of_speech.VERB],
      "Other": [spacy.parts_of_speech.X, spacy.parts_of_speech.EOL]
    }

    counts = {key:0 for key in parts_of_speech}

    for token in doc:
      for name, tags in parts_of_speech.items():
        if token.pos in tags:
          counts[name] += 1

    return counts
