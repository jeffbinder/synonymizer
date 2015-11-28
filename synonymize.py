import codecs
import random
import sys

try:
    infile = sys.argv[1]
    outfile = sys.argv[2]
except:
    print 'Usage: {0} <infile> <outfile>'.format(sys.argv[0])
inf = codecs.open(infile, 'r', 'utf8')
outf = codecs.open(outfile, 'w', 'utf8')

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'[\w&]([\w&\']*[\w&])?|\S|\s')

from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

from nltk.corpus import wordnet as wn
from nltk import pos_tag

import en

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wn.ADJ
    elif treebank_tag.startswith('V'):
        return wn.VERB
    elif treebank_tag.startswith('N'):
        return wn.NOUN
    elif treebank_tag.startswith('R'):
        return wn.ADV
    else:
        return None

def lemmatize(word, pos):
    try:
        if pos.startswith('J'):
            return word, None, None
        elif pos.startswith('V'):
            return en.verb.present(word), en.verb.tense(word), None
        elif pos.startswith('N'):
            return en.noun.singular(word), None, en.noun.singular(word) != word
        elif pos.startswith('R'):
            return word, None, None
        else:
            return word, None, None
    except KeyError:
        return word, None, None

def get_synonyms(word, pos):
    synonyms = []
    word_lemma, tense, is_plural = lemmatize(word, pos)
    wordnet_pos = get_wordnet_pos(pos)
    for synset in wn.synsets(word_lemma, pos=wordnet_pos):
        for synset_lemma in synset.lemmas():
            new_word = synset_lemma.name()
            new_word_parts = new_word.split('_')
            if tense:
                try:
                    new_word_parts[0] = en.verb.conjugate(new_word_parts[0], tense)
                except KeyError:
                    pass
            if is_plural:
                try:
                    new_word_parts[0] = en.noun.plural(new_word_parts[0])
                except KeyError:
                    pass
            new_word = '_'.join(new_word_parts)
            synonyms.append(new_word)
    return synonyms

def random_synonym(word, pos):
    if word.lower() in stopwords:
        return word
    synonyms = get_synonyms(word, pos)
    if not synonyms:
        return word
    syn = random.choice(synonyms)
    syn = syn.replace('_', ' ')
    if word[0].isupper():
        if len(word) > 1 and word[1].isupper():
            syn = syn.upper()
        else:
            syn = syn[0].upper() + syn[1:]
    else:
        syn = syn.lower()
    return syn

def get_antonyms(word, pos):
    synonyms = []
    word_lemma, tense, is_plural = lemmatize(word, pos)
    wordnet_pos = get_wordnet_pos(pos)
    for synset in wn.synsets(word_lemma, pos=wordnet_pos):
        for synset_lemma in synset.lemmas():
            new_word = synset_lemma.name()
            if tense:
                try:
                    new_word = en.verb.conjugate(new_word, tense)
                except KeyError:
                    pass
            if is_plural:
                try:
                    new_word = en.noun.plural(new_word)
                except KeyError:
                    pass
            synonyms.append(new_word)
    return synonyms

def random_antonym(word, pos):
    if word.lower() in stopwords:
        return word
    synonyms = get_synonyms(word, pos)
    if not synonyms:
        return word
    syn = random.choice(synonyms)
    syn = syn.replace('_', ' ')
    if word[0].isupper():
        if len(word) > 1 and word[1].isupper():
            syn = syn.upper()
        else:
            syn = syn[0].upper() + syn[1:]
    else:
        syn = syn.lower()
    return syn

for line in inf.readlines():
    toks = tokenizer.tokenize(line)
    toks_pos = pos_tag(toks)
    new_toks = [random_synonym(tok, pos) for tok, pos in toks_pos]
    outf.write(''.join(new_toks))

