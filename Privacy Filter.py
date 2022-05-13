import spacy
from spacy import displacy

NER = spacy.load("en_core_web_sm")

raw_text = "The Indian Space Research Organisation or is the national space agency of India, headquartered in Bengaluru. It operates under Department of Space which is directly overseen by the Prime Minister of India while Chairman of ISRO acts as executive of DOS as well."

text1 = NER(raw_text)

l = {}

for word in text1.ents:
    #print(word.text, word.label_)
    l[word.text] = word.label_

from collections import OrderedDict
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

private_text = replace_all(raw_text, l)
print(private_text)
