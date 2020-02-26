# # USAGE
# ** Locally Installed scikit: from `src` directory:
# python bayes_classifier.py
# ** Docker Container: from a6_bayes:
# docker run --rm -v $(pwd)/src:/root opencv python bayes_classifier.py

# ref:https://jakevdp.github.io/PythonDataScienceHandbook/05.05-naive-bayes.html

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix

categories = ['talk.religion.misc', 'soc.religion.christian',
              'sci.space', 'comp.graphics']
train = fetch_20newsgroups(subset='train', categories=categories)
test = fetch_20newsgroups(subset='test', categories=categories)

print(train.data[1])

# TfidfVectorizer converts a collection of raw documents to a matrix of TF-IDF
# features, where TF is the Term Frequency that summarizes how often a given
# word appears within a document, and IDF is the Inverse Document Frequency
# downscales words that appear a lot across documents.

model = make_pipeline(TfidfVectorizer(), MultinomialNB())

model.fit(train.data, train.target)
labels = model.predict(test.data)

mat = confusion_matrix(test.target, labels)
fig = plt.figure(figsize=(9, 5))
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=train.target_names, yticklabels=train.target_names)
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.savefig('heatmap.png')
