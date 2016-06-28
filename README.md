# devcon-word-cloud
Word cloud generated from Cerner Devcon 2016 submissions

Example output:
![Wordcloud](./cloud.png)

# How to run
requires brew, pip, and python 2.7 installed

to get wordcloud working:

install pillow dependencies:

> brew install freetype libpng libjpeg

if anything is unlinked; link it, for example:

> brew link freetype

if that throws an error run this to fix permissions for brew first:

> sudo chown -R \`whoami\`:admin /usr/local/lib/pkgconfig

install pillow, a dependency for wordcloud:
> sudo pip install pillow

install wordcloud:
> sudo pip install wordcloud

install nltk for lemmatization
> sudo pip install nltk

open a python console and enter
> nltk.download()

This opens a downloader for corpora nltk relies on. Download the 'Wordnet' corpora.

Place data in a file named: `submissions.txt`

Normalize submission data:
> python clean_submissions.py

Create word cloud:
> python word_cloud.py