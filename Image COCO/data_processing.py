from collections import Counter
import io
import re
import pickle


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


f = open("CommentsMay2017_text.txt", "r")
data = f.read()

# data = cleanhtml(data)
# print(data)

words = [x for x in data.split(' ') if x != '']
sentences = [x for x in data.split('.') if x != '' and x != ' ' and x != '\n']


print(sentences)


# ignored_words = set()
# for k, v in word_freq.items():
#     if word_freq[k] < MIN_WORD_FREQUENCY:
#         ignored_words.add(k)
#
# words = set(text_in_words)
# print('Unique words before ignoring:', len(words))
# print('Ignoring words with frequency <', MIN_WORD_FREQUENCY)
# words = sorted(set(words) - ignored_words)
# print('Unique words after ignoring:', len(words))
#
# word_indices = dict((c, i) for i, c in enumerate(words))
# indices_word = dict((i, c) for i, c in enumerate(words))
#
# STEP = 1
# sentences = []
# next_words = []
# ignored = 0
# for i in range(0, len(text_in_words) - SEQUENCE_LEN, STEP):
#     # Only add sequences where no word is in ignored_words
#     if len(set(text_in_words[i: i+SEQUENCE_LEN+1]).intersection(ignored_words)) == 0:
#         sentences.append(text_in_words[i: i + SEQUENCE_LEN])
#         next_words.append(text_in_words[i + SEQUENCE_LEN])
#     else:
#         ignored = ignored+1


counts = Counter(words)

#print((counts.items()))
print(f"Unic words: {len(counts.keys())}")
print(f"Unic words: {len(set(words))}")

pickle_out = open("NYT_key_val.pickle", "wb")

pickle.dump(list(counts.items()), pickle_out)
pickle_out.close()

pickle_in = open("NYT_key_val.pickle","rb")
example_dict = pickle.load(pickle_in)
#print(example_dict)



f = open("NYT_key_val.txt", "w")
f.write(' '.join([str(x) for x in counts.values()]))
f.close()