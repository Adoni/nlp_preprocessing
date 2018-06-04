# encoding: utf-8
"""
    segment_Chinese_word.py
    ~~~~~~~~~
    
    Chinese segmentation
    
    :author: Xiaofei Sun
    :contact: adoni1203@gmail.com
    :date: 2018/6/2
    :license: MIT, see LICENSE for more details.
"""

from pyltp import Segmentor
from tqdm import tqdm
import argparse


parser = argparse.ArgumentParser(description='Words Segmentation in Chinese')
parser.add_argument('--input', type=str, help='path of corpus file')
parser.add_argument('--output', type=str, help='path of output file')
parser.add_argument('--model-path', type=str, help='path to ltp model, cws.model')
args = parser.parse_args()

segmentor = Segmentor()
segmentor.load(args.model_path)
sentences = []
with open(args.input, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        sentences.append(line)
segmented_sentences = []

for sentence in tqdm(sentences):
    words = segmentor.segment(sentence)
    segmented_sentences.append(" ".join(words))

with open(args.output, "w", encoding="utf-8") as f:
    f.write("\n".join(segmented_sentences))
segmentor.release()
