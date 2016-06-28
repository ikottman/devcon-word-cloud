from nltk.stem import WordNetLemmatizer
import string


class SubmissionCleaner:
    @staticmethod
    def combine_similar_words(words_list):
        lemmatizer = WordNetLemmatizer()
        reduced_list = []
        # find the lemma of each word
        for word in words_list:
            reduced_list.append(lemmatizer.lemmatize(word))

        return reduced_list

    @staticmethod
    def lowercase_and_remove_punctuation(text):
        # lower case for obvious reasons
        text = text.lower()

        # remove all contractions to prevent situations like "we'll" becoming "we" and "ll"
        # normally a regex tokenizer could be used for this but that assumes single quote is only ever used
        # in contractions
        with open("./resources/contractions.txt", "r") as file:
            contractions = file.read().splitlines()
            for contraction in contractions:
                text = text.replace(contraction, "")

        # replace all punctuation with spaces. This prevents mishandling of special cases such as
        # hyphenated-words and/or websites.com
        for char in set(string.punctuation):
            text = text.replace(char, " ")

        return text
