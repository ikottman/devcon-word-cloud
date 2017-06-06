from text_cleaner import TextCleaner as Cleaner
from collections import Counter
import re

from random import shuffle

# read all submissions into a single string
submissions_string = open('./submissions.txt').read()

# lower case and remove punctuation
submissions_string = Cleaner.lowercase_and_remove_punctuation(submissions_string)

# get list of all words
submission_words = re.sub("[^\w]", " ", submissions_string).split()
print "Total words:", len(submission_words)

# filter out common words to reduce noise
stopwords = open('./resources/stopwords.txt').read()
stopwords_set = set(stopwords.split("\n"))
filtered_word_list = [w for w in submission_words if w not in stopwords_set]
print "Total words after stopword filtering:", len(filtered_word_list)

# write word counts
word_counts = Counter(filtered_word_list)
print "Distinct words:", len(word_counts)
with open("./data/word_counts.txt", "w") as file:
    for tuple in word_counts.most_common():
        file.write('%s : %d \n' % (tuple[0], tuple[1]))

# combine similar words using lemmatization
lemmatized = Cleaner.combine_similar_words(filtered_word_list)
lemmatized_word_counts = Counter(lemmatized)
print "Distinct words after lemmatization:", len(lemmatized_word_counts)

# write word counts after lemmatization
with open("./data/word_counts_after_lemmatization.txt", "w") as file:
    for tuple in lemmatized_word_counts.most_common():
        file.write('%s : %d \n' % (tuple[0], tuple[1]))

# write out final data set
with open("./data/cleaned_data.txt", "w") as file:
    for word in lemmatized:
        file.write(word + "\n")