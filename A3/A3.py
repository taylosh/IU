#!/usr/bin/env python3
"""
LING545/CS659 A3: Part-of-Speech (POS) Tagging using Hidden Markov Models (HMMs)
@author: Shuju Shi

In this assignment, you will implement HMMs for POS Tagging using an English corpus.
"""

### Import libraries
from collections import defaultdict
import os
import re
import math
from sklearn.metrics import accuracy_score, f1_score
import numpy as np

def read_corpus(corpus):
    """
    Read the tagged corupus into a list contains (word, tag) pairs for each sentence
    :param corpus: a file contains (word tag) sequences
    :return: a list contains lists of (word, tag) sequences by sentences
    """
    all_word2tag= [] # (word, tag) pairs for all sentences in the corpus
    with open(corpus, "r") as c:
        one_word2tag = [] # (word, tag) pairs for each sentences in the corpus
        ### Start your implementation here
        pass
    return all_word2tag

def learn_hmm_compo(train_word2tag, k=0.1):
    """
    Given the training corpus, learn the initial, emission and transition probabilities
    :param train_word2tag:
    :return:
    """
    initial_count = defaultdict(float)
    transition_count = defaultdict(lambda: defaultdict(float))
    emission_count = defaultdict(lambda: defaultdict(float))
    words = set()
    tags = set()
    #### start your implementation here
    ### complete the implementation of initial_count, transition_count and emission count

    ### add the "<UNK>" token to words
    words.add("<UNK>")

    ### add k (k=0.1) smoothing


    ### calculate probabilities , convert to logrithm
    initial_prob = ...
    transition_prob = ...
    emission_prob = ...
    return tags, words, initial_prob, transition_prob, emission_prob

def viterbi(sentence, tags, words, initial_prob, transition_prob, emission_prob):
    # Initialize Viterbi and backpointer tables
    viterbi = defaultdict(lambda: defaultdict(float))
    backpointer = defaultdict(lambda: defaultdict(str))
    word_ls = []
    gold_tags = []

    # For the first word
    first_word = sentence[0][0] if sentence[0][0] in words else "<UNK>"
    word_ls.append(sentence[0][0])
    gold_tags.append(sentence[0][1])

    for tag in tags:
        viterbi[tag][0] = initial_prob[tag] + emission_prob[tag][first_word]
        backpointer[tag][0] = "<start>"

    # Recursion: fill in the Viterbi table
    for t in range(1, len(sentence)):
        word = sentence[t][0] if sentence[t][0] in words else "<UNK>"
        word_ls.append(word)
        gold_tags.append(sentence[t][1])
        for curr_tag in tags:
            max_prob, best_prev_tag = max(
                [(viterbi[prev_tag][t - 1] + transition_prob[prev_tag][curr_tag] +
                  emission_prob[curr_tag][word], prev_tag) for prev_tag in tags],
                key=lambda x: x[0]
            )
            viterbi[curr_tag][t] = max_prob
            backpointer[curr_tag][t] = best_prev_tag

    # Termination step
    pred_tags = []
    max_final_prob, best_final_tag = max(
        [(viterbi[tag][len(sentence) - 1], tag) for tag in tags],
        key=lambda x: x[0]
    )
    pred_tags.append(best_final_tag)
    # Backtrack to find the best tag sequence
    for t in range(len(sentence) - 1, 0, -1):
        pred_tags.insert(0, backpointer[pred_tags[0]][t])

    return word_ls, gold_tags, pred_tags

def hmm_tagging(test_corpus, tags, words, initial_prob, transition_prob, emission_prob):
    """
    Use the HMM components and viterbi algorithm to tag the sentences and return the final results (Accuracy, F1 score).
    :param test_corpus:
    :param tags:
    :param words:
    :param initial_prob:
    :param transition_prob:
    :param emission_prob:
    :return:
    """
    ### start your implementation here
    acc = ...
    f1 = ...
    pass

    return acc, f1
if __name__ == "__main__":

    input_dir = "./pos_eng"

    train_word2tag = read_corpus(os.path.join(input_dir, "en_ewt-ud-train.csv"))
    test_word2tag = read_corpus(os.path.join(input_dir, "en_ewt-ud-test.csv"))



    tags, words, initial_prob, transition_prob, emission_prob = learn_hmm_compo(train_word2tag, k=0.1)
    word_ls, gold_tags, pred_tags = viterbi(train_word2tag[0], tags, words, initial_prob, transition_prob, emission_prob)

    acc, f1 = hmm_tagging(test_word2tag, tags, words, initial_prob, transition_prob, emission_prob)




