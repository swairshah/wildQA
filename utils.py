from colorama import Fore, Back, Style
from collections import defaultdict
from heapq import heappush, heappop
import string

def highlight_match(text, query, tokenizer=None):

    if tokenizer == None:
        tokenizer = lambda x : x.strip(string.punctuation).split()
    highlight_indices = []

    for w in tokenizer(query):
        loc = text.find(w)
        if loc > -1:
            end_loc = loc+len(w)
            heappush(highlight_indices, (loc, end_loc))

    highlighted_text = ""
    prev_end = 0
    for i in range(len(highlight_indices)):
        loc, end_loc = heappop(highlight_indices)
        highlighted_text += text[prev_end:loc]+Fore.GREEN+text[loc:end_loc]+Style.RESET_ALL
        prev_end=end_loc

    return highlighted_text
