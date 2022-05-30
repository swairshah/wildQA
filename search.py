import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

from rank_bm25 import BM25Okapi

from sentence_transformers import SentenceTransformer, CrossEncoder
import sentence_transformers.util

import string
string.punctuation += '“”'
from io import StringIO

from utils import highlight_match, page_parser, overlapping_paragraph_generator

def bm25_tokenizer(text):
    tokenized_text = []
    stemmer = nltk.stem.SnowballStemmer('english')
    for token in word_tokenize(text):
        token = token.strip(string.punctuation)
        if len(token) > 0 and token not in ENGLISH_STOP_WORDS:
            token = stemmer.stem(token)
            tokenized_text.append(token)

    return tokenized_text

class DocSearch:
    def __init__(self, fname, parse_type='page'):
        self.fname = fname
        pages = page_parser(self.fname)
        self.pages = overlapping_paragraph_generator(pages)

        self.bm25_tokenizer = bm25_tokenizer
        self.bm25_tokenized_corpus = [bm25_tokenizer(page) for page in self.pages]
        self.bm25 = BM25Okapi(self.bm25_tokenized_corpus)

    def bm25_search(self, query, n=5):
        tokenized_query = self.bm25_tokenizer(query)
        doc_scores = self.bm25.get_scores(tokenized_query)
        results = self.bm25.get_top_n(tokenized_query, self.pages, n)
        return results

if __name__ == "__main__":
    fname = 'data/driverguide.pdf'
    doc = DocSearch(fname)
    query = "what is the driving speed limit within a school zone?"
    results = doc.bm25_search(query)
    for result in results:
        print(highlight_match(result, query))
        print('------------------')

