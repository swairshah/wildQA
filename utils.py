from colorama import Fore, Back, Style
from collections import defaultdict
from heapq import heappush, heappop
import string
import re
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

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

def page_parser(fname: str):
    PAGE_SEP = '<PAGE>'
    output_string = StringIO()
    with open(fname, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
            output_string.write(PAGE_SEP)

    data = output_string.getvalue()
    pages = data.split(PAGE_SEP)
    return pages

def overlapping_paragraph_generator(pages, size=300, overlap=50):

    def chunk(lst, n, k):
        n = min(n, len(lst)-1)
        return [lst[i:i+n] for i in range(0, len(lst) - n+1, n-k)]

    doc = '<PAGE>'.join(pages)	
    words = [l for l in re.split('\.|\n|\ ', doc) if l]

    ret = [' '.join(line_set) for line_set in chunk(words, size, overlap)]

    return ret

def paragraph_parser(fname):
    pass

