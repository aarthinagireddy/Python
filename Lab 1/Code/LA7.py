import nltk
from nltk.stem import WordNetLemmatizer
from nltk.util import trigrams

file = open('nlp_input.txt').read()
tokens = nltk.word_tokenize(file)
for i in tokens:
    print(i)
lm = WordNetLemmatizer()
lm_words = [lm.lemmatize(w) for w in tokens]
print(lm_words)

# find all trigrams
trigrams = trigrams(lm_words)

from collections import defaultdict
trigram_dictionaries = defaultdict(int)
for x in trigrams:
    trigram_dictionaries[x] += 1

trigrams_top10 = sorted(trigram_dictionaries.items(), key=lambda x: x[1], reverse=True)[:10]
print('Top ten trigrams')
print(trigrams_top10)

# extracting all the sentences in the file
s_t = nltk.sent_tokenize(file)


s = [sentence for trigram in trigrams_top10 for sentence in s_t if ' '.join(trigram[0]) in sentence]
print('sentences that contain the trigrams')
print(' '.join(s))