import spacy

nlp = spacy.load('en')
filename = 'Tripadvisor_hotelreviews_Shivambansal.txt'


document = unicode(open(filename).read().decode('utf8'))
document = nlp(document)

# print(dir(document))
#
# print(document[0])
#
# print(document[len(document)-5])
#
# print(list(document.sents))
#
# all_tags = {w.pos: w.pos_ for w in document}
# print(all_tags)
#
# for word in list(document.sents)[0]:
#     print(word, word.tag_)

# Define some parameters
noisy_pos_tags = ['PROP']
min_token_length = 2


# Function to check if the token is a noise or not
def isNoise(token):
    is_noise = False
    if token.pos_ in noisy_pos_tags:
        is_noise = True
    elif token.is_stop == True:
        is_noise = True
    elif len(token.string) <= min_token_length:
        is_noise = True
    return is_noise


def cleanup(token, lower = True):
    if lower:
        token = token.lower()
    return token.strip()


# Top unigrams used in the reviews
from collections import Counter
cleaned_list = [cleanup(word.string) for word in document if not isNoise(word)]
print(Counter(cleaned_list) .most_common(5))

# Entity detection
labels = set([w.label_ for w in document.ents])
for label in labels:
    entities = [cleanup(e.string, lower=False) for e in document.ents if label == e.label_]
    entities = list(set(entities))
    print(label, entities)
