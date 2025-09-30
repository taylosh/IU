#!/usr/bin/env python3
"""
LING545/CS659 A1: N-gram language models
@author: taylosh


"""
### import the libraries
import numpy as np
from collections import defaultdict

def load_dict(file):
    """
    This function loads the file storing mapping from words to their corresponding indices.
    :param file: The file that contains the mapping from words to their corresponding indices.
    :return: A dictionary with keys being words and values being their corresponding indices.
    """
    word_to_index = {}
    with open(file, 'r') as f:
        for line in f:
            word, index = line.strip().split()
            word_to_index[word] = int(index)
    return word_to_index


def get_unigram(file, dict):
    """
    This function calculates the unigram counts and unigram probabilities
    :param file: input text file for unigram calculation
    :param dict: a dictionary maps from words to indices
    :return:
    1. a vector of shape N*1 of unigram counts, N = len(dict.keys())
    2. a vector of shape N*1 of unigram probabilities, N = len(dict.keys())
    """
    N = len(dict.keys())
    unigram_c = np.zeros(N)  # Change to 1D array for unigram counts
    
    with open(file, 'r') as f:
        for line in f:
            words = line.strip().split()
            for word in words:
                if word in dict:
                    index = dict[word]
                    unigram_c[index] += 1 

    total_words = np.sum(unigram_c)  # Total count of all words
    
    # Calculate unigram probabilities
    unigram_p = unigram_c / total_words if total_words > 0 else np.zeros(N)

    return unigram_c, unigram_p

def get_bigram(file, dict, unigram_c):
    """
    This function calculates the bigram counts and bigram probabilities
    :param file: input text file for bigram calculation
    :param dict: a dictionary maps from words to indices
    :param unigram_c: a vector of shape N*1 of unigram counts, N = len(dict.keys())
    :return:
    1. a matrix of shape N*N of bigram counts, N = len(dict.keys())
    2. a matrix of shape N*N of bigram probability, N = len(dict.keys())
    """
    N = len(dict.keys())
    bigram_c = np.zeros((N, N))
    
    # Count bigrams
    with open(file, 'r') as f:
        for line in f:
            words = line.strip().split()
            for i in range(len(words) - 1):
                w1, w2 = words[i], words[i+1]
                if w1 in dict and w2 in dict:
                    index1 = dict[w1]
                    index2 = dict[w2]
                    bigram_c[index1, index2] += 1

    # Calculate bigram probabilities
    bigram_p = np.zeros_like(bigram_c)
    for i in range(N):
        bigram_p[i] = bigram_c[i] / unigram_c[i] if unigram_c[i] > 0 else 0

    return bigram_c, bigram_p


def get_bigram_k(file, dict, unigram_c, k):
    """
    This function calculates the bigram probabilities with add-k smoothing.
    :param file: input text file for bigram calculation
    :param dict: a dictionary maps from words to indices
    :param unigram_c:a vector of shape N*1 of unigram counts, N = len(dict.keys())
    :param k: a parameter for add-k smoothing with a default value of 0.1,  0=<k<=1
    :return:
    a matrix of shape N*N of bigram probability with add-k smoothing, N = len(dict.keys())
    """
    N = len(dict.keys())
    bi_c = np.zeros((N, N))
    
    with open(file, 'r') as f:
        for line in f:
            words = line.strip().split()
            for i in range(len(words) - 1):
                w1, w2 = words[i], words[i+1]
                if w1 in dict and w2 in dict:
                    index1 = dict[w1]
                    index2 = dict[w2]
                    bi_c[index1, index2] += 1

    V = len(dict.keys())  # Vocabulary size
    bi_p_k = np.zeros_like(bi_c)
    
    for i in range(N):
        bi_p_k[i] = (bi_c[i] + k) / (unigram_c[i] + k * V) if unigram_c[i] > 0 else (bi_c[i] + k) / k

    return bi_p_k


def infer(sen, unigram_p, bi_p, bi_p_k, dict_word2index):
    """
    Given a sentence, this function calculates the probability of the sentence using unigram, bigram and bigram with add-k smoothing.
    :param sen: A given sample of sentence.
    :param unigram_p: a vector of shape N*1 of unigram probabilities, N = len(dict.keys())
    :param bi_p: a matrix of shape N*N of bigram probability, N = len(dict.keys())
    :param bi_p_k: a matrix of shape N*N of bigram probability with add-k smoothing, N = len(dict.keys())
    :param dict_word2index: A dictionary with keys being words and values being their corresponding indices.
    :return:
    1. sen_uni_p: The probability of the given sentence using unigram.
    2. sen_bi_p: The probability of the given sentence using bigram.
    3. sen_bik_p: The probability of the given sentence using bigram with add-k smoothing.
    """
    ws = sen.strip().split()
    #Number of unique words for verifyin that all expected words are included in the dicts & matrices
    N = len(dict_word2index) 
    
    # Initialize probabilities
    sen_uni_p = 1.0
    sen_bi_p = 1.0
    sen_bik_p = 1.0
    
    # Compute unigram probability
    for word in ws:
        if word in dict_word2index:
            index = dict_word2index[word]
            sen_uni_p *= unigram_p[index]
        else:
            sen_uni_p = 0
            break
    
    # Compute bigram probability
    for i in range(len(ws) - 1):
        w1, w2 = ws[i], ws[i+1]
        if w1 in dict_word2index and w2 in dict_word2index:
            index1 = dict_word2index[w1]
            index2 = dict_word2index[w2]
            sen_bi_p *= bi_p[index1, index2]
        else:
            sen_bi_p = 0
            break
    
    # Compute bigram probability with add-k smoothing
    for i in range(len(ws) - 1):
        w1, w2 = ws[i], ws[i+1]
        if w1 in dict_word2index and w2 in dict_word2index:
            index1 = dict_word2index[w1]
            index2 = dict_word2index[w2]
            sen_bik_p *= bi_p_k[index1, index2]
        else:
            sen_bik_p = 0
            break

    return sen_uni_p, sen_bi_p, sen_bik_p

if __name__ == "__main__":

    ### load the mapping from word to their correponding indices
    text_dict = "word2index.txt"
    dict_word2index = load_dict(text_dict)

    ### directory to the text file for n-gram calculation
    text = "./all_dev.txt"

    ### unigram calcualtion
    unigram_c, unigram_p = get_unigram(text, dict_word2index)

    ### bigram calcualtion
    bi_c, bi_p = get_bigram(text, dict_word2index, unigram_c)

    ### bigram calculation with add-k smoothing
    bi_p_k = get_bigram_k(text, dict_word2index, unigram_c, k=0.1)

    #############Infer the probability of the following sentences using unigram, bigram and bigram with add-k
    ### Sen 1: I beleive a group tour is interesting.
    ### Sen 2: I believe that a group tour is interesting
    ### Notice that in Sen 1, 'believe' was spelled incorrectly.

    sen1 = "<s> I beleive that a group tour is interesting . <\s>"
    sen2 = "<s> I believe that a group tour is interesting . <\s>"
    sen_uni_p1, sen_bi_p1, sen_bik_p1 = infer(sen1, unigram_p, bi_p, bi_p_k, dict_word2index)
    sen_uni_p2, sen_bi_p2, sen_bik_p2 = infer(sen2, unigram_p, bi_p, bi_p_k, dict_word2index)

    ### save the probability result into a text file named prob_result.txt,  following the format below
    # sen1, sen_uni_p, sen_bi_p, sen_bik_p
    # sen2, sen_uni_p, sen_bi_p, sen_bik_p
    with open('prob_result.txt', 'w') as f:
        f.write(f"Sen 1: {sen1}, Unigram Probability: {sen_uni_p1}, Bigram Probability: {sen_bi_p1}, Bigram with Add-K Probability: {sen_bik_p1}\n")
        f.write(f"Sen 2: {sen2}, Unigram Probability: {sen_uni_p2}, Bigram Probability: {sen_bi_p2}, Bigram with Add-K Probability: {sen_bik_p2}\n")


    ### In the same txt file (prob_result.txt), answer the following question:
    # The current corpus contains essays written by second language learners, if the n-grams
    # are trained using essays by native speakers, how would you expect the probability of
    # each sentence change and why?