# encoding: utf-8
"""
    train_valid_test_split.py
    ~~~~~~~~~
    
    Model description
    
    :author: Xiaofei Sun
    :contact: adoni1203@gmail.com
    :date: 2018/6/4
    :license: MIT, see LICENSE for more details.
"""



from tqdm import tqdm
import argparse
import os
import numpy


parser = argparse.ArgumentParser(description='Shuffle dataset into train, valid and test')
parser.add_argument('--input', type=str, help='path of corpus file')
parser.add_argument('--output', type=str, help='path of output file')
parser.add_argument('--save-order-to', type=str, default='', help='path of order')
parser.add_argument('--load-order-from', type=str, default='', help='path of order, use random order if it is empty')
args = parser.parse_args()

sentences = []
with open(args.input, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        sentences.append(line)

if args.load_order_from == '':
    order = list(range(len(sentences)))
    numpy.random.shuffle(order)
else:
    with open(args.load_order_from, "r", encoding="utf-8") as f:
        order = [int(line.strip()) for line in f]

sentences = [sentences[i] for i in order]

train_ratio = 0.8
valid_ratio = 0.1
test_ratio = 0.1

train_count = int(len(sentences) * train_ratio)
valid_count = int(len(sentences) * valid_ratio)

with open(os.path.join(args.output, "train.txt"), "w", encoding="utf-8") as f:
    f.write('\n'.join(sentences[:train_count]))
with open(os.path.join(args.output, "valid.txt"), "w", encoding="utf-8") as f:
    f.write('\n'.join(sentences[train_count:train_count+valid_count]))
with open(os.path.join(args.output, "test.txt"), "w", encoding="utf-8") as f:
    f.write('\n'.join(sentences[train_count+valid_count:]))

if args.save_order_to != '':
    order = [str(i) for i in order]
    with open(args.save_order_to, "w", encoding="utf-8") as f:
        f.write('\n'.join(order))

