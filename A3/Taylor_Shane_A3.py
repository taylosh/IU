#!/usr/bin/env python3
"""
LING545/CS659 A3: Part-of-Speech (POS) Tagging using Hidden Markov Models (HMMs)
@author: taylosh 

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
    all_word2tag= [] # (word, tag) pairs for all sentences
    with open(corpus, "r") as c:
        one_word2tag = [] # (word, tag) pairs for each sentence
        for line in c:
            line = line.strip()
            if not line:  # If blank, end
                if one_word2tag:
                    all_word2tag.append(one_word2tag)
                    one_word2tag = []
            else:
                word, tag = line.split()
                one_word2tag.append((word, tag))
        if one_word2tag:  # Add last sentence if file doesn't end with blank
            all_word2tag.append(one_word2tag)
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

    for sentence in train_word2tag:
        prev_tag = None
        for i, (word, tag) in enumerate(sentence):
            words.add(word)
            tags.add(tag)

            # Initial count for first word's tag in sentence
            if i == 0:
                initial_count[tag] += 1
            
            # Transition counts
            if prev_tag is not None:
                transition_count[prev_tag][tag] += 1
            prev_tag = tag
            
            # Emission counts
            emission_count[tag][word] += 1

    ### add the "<UNK>" token
    words.add("<UNK>")

    ### calculate probabilities , convert to log, with k=0.1 smoothing
    initial_prob = {tag: math.log((initial_count[tag] + k) / (sum(initial_count.values()) + k * len(tags)))
                    for tag in tags}

    transition_prob = {prev_tag: {tag: math.log((transition_count[prev_tag][tag] + k) /
                                                (sum(transition_count[prev_tag].values()) + k * len(tags)))
                                  for tag in tags}
                       for prev_tag in tags}

    emission_prob = {tag: {word: math.log((emission_count[tag][word] + k) /
                                          (sum(emission_count[tag].values()) + k * len(words)))
                           for word in words}
                     for tag in tags}
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
    pred_tags_all = []
    gold_tags_all = []

    for sentence in test_corpus:
        word_ls, gold_tags, pred_tags = viterbi(sentence, tags, words, initial_prob, transition_prob, emission_prob)
        pred_tags_all.extend(pred_tags)
        gold_tags_all.extend(gold_tags)

    acc = accuracy_score(gold_tags_all, pred_tags_all)
    f1 = f1_score(gold_tags_all, pred_tags_all, average="weighted")

    return acc, f1


if __name__ == "__main__":
    input_dir = "./pos_eng"

    # Load and process corpus
    train_word2tag = read_corpus(os.path.join(input_dir, "en_ewt-ud-train.csv"))
    test_word2tag = read_corpus(os.path.join(input_dir, "en_ewt-ud-test.csv"))

    # Train HMM parameters
    tags, words, initial_prob, transition_prob, emission_prob = learn_hmm_compo(train_word2tag, k=0.1)

    # Tag a sample sentence from the training set (optional check)
    word_ls, gold_tags, pred_tags = viterbi(train_word2tag[0], tags, words, initial_prob, transition_prob, emission_prob)

    # Run HMM tagger on test corpus
    acc, f1 = hmm_tagging(test_word2tag, tags, words, initial_prob, transition_prob, emission_prob)
    
    # Print accuracy and F1 scores
    print(f"Accuracy: {acc * 100:.2f}%")
    print(f"F1 Score (weighted): {f1:.4f}")
    
    # Identify/ analyze tagging errors
    error_counts = defaultdict(int)
    word_error_counts = defaultdict(lambda: defaultdict(int))

    for sentence in test_word2tag:
        _, gold_tags, pred_tags = viterbi(sentence, tags, words, initial_prob, transition_prob, emission_prob)
        for i, (word, gold_tag, pred_tag) in enumerate(zip(sentence, gold_tags, pred_tags)):
            if gold_tag != pred_tag:
                error_counts[(gold_tag, pred_tag)] += 1
                word_error_counts[word[0]][(gold_tag, pred_tag)] += 1

    # Display most common tagging errors
    print("\nMost Common Tagging Errors (Gold->Predicted:Quantity):")
    for (gold, pred), count in sorted(error_counts.items(), key=lambda item: item[1], reverse=True)[:10]:
        print(f"{gold} → {pred}: {count} times")

    # Display most frequently mis-tagged words
    print("\nWords Most Frequently Tagged Incorrectly:")
    for word, errors in sorted(word_error_counts.items(), key=lambda item: sum(item[1].values()), reverse=True)[:10]:
        print(f"{word}: {dict(errors)}")

