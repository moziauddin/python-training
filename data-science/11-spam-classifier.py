import os
import io
import numpy as np
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def read_files(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)

            in_body = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if in_body:
                    lines.append(line)
                elif line == '\n':
                    in_body = True
            f.close()
            message = '\n'.join(lines)
            yield path, message

def dataframe_from_dir(path, classification):
    rows = []
    index = []
    for filename, message in read_files(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)
    return DataFrame(rows, index=index)

data = DataFrame({'message': [], 'class': []})
data = data.append(dataframe_from_dir('C:\zData\Practice\data-science\emails\spam', 'spam'))
data = data.append(dataframe_from_dir('C:\zData\Practice\data-science\emails\ham', 'ham'))

print(data.head())

vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)

classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)
print('COUNTS:', counts)
print('TARGETS:', targets)

example_body = ['Free Viagra Now!!!', 'How are you feeling tonight!!!', "Hi there", 'FREE']
example_counts = vectorizer.transform(example_body)
prediction = classifier.predict(example_counts)
print(prediction)