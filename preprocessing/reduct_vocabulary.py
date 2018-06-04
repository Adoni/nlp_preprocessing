# encoding: utf-8
"""
Model Description

@author: Xiaofei Sun
@contact: adoni1203@gmail.com
@version: 0.1
@license: Apache Licence
@file: reduct_vocabulary.py
@time: 2018/6/4
"""



from tqdm import tqdm
import argparse
from tqdm import tqdm


parser = argparse.ArgumentParser(description='Replace some unusal word with <unk>')
parser.add_argument('--input', type=str, help='path of corpus file')
parser.add_argument('--output', type=str, help='path of output file')
parser.add_argument('--vocab-size', type=int, help='vocabulary size')
args = parser.parse_args()

sentences = []
with open(args.input, "r", encoding="utf-8") as f:
    for line in tqdm(f):
        line = line.strip()
        if line == "":
            continue
        sentences.append(line.split(' '))

word_count = dict()
for sentence in tqdm(sentences):
    for word in sentence:
        try:
            word_count[word] += 1
        except:
            word_count[word] = 1
word_count = sorted(word_count.items(), key=lambda x: x[1])
print(len(word_count))

words = set(word[0] for word in word_count[-args.vocab_size:])

new_sentences = []

for i in range(len(sentences)):
    for j in range(len(sentences[i])):
        if sentences[i][j] not in words:
            sentences[i][j] = "<unk>"
    sentences[i] = " ".join(sentences[i])

with open(args.output, "w", encoding="utf-8") as f:
    f.write('\n'.join(sentences))
