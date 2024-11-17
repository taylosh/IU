#!/usr/bin/env python3
"""
LING545/CS659 A1: N-gram language models
@author: Shuju Shi
"""
############################
# In this assignment, you will implement n-gram (unigram, bigram and bigram with add-k smoothing)  language models.


### import the libraries
import numpy as np
from collections import defaultdict

def load_dict(file):
    """
    This function loads the file storing mapping from words to their corresponding indices.
    :param file: The file that contains the mapping from words to their corresponding indices.
    :return: A dictionary with keys being words and values being their corresponding indices.
    """

    ### Start your implementation here

    pass


def get_unigram(file, dict):
    """
    This function calculates the unigram counts and unigram probabilities
    :param file: input text file for unigram calculation
    :param dict: a dictionary maps from words to indices
    :return:
    1. a vector of shape N*1 of unigram counts, N = len(dict.keys())
    2. a vector of shape N*1 of unigram probabilities, N = len(dict.keys())
    """

    unigram_c = np.zeros(len(dict))

    ### Start your implementation here
    pass


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
    bigram_c = np.zeros((len(dict.keys()),len(dict.keys())))


    ### Start your implementation here
    pass


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
    bi_c = np.zeros((len(dict.keys()),len(dict.keys())))

    ### Start your implementation here
    pass


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
    ws = sen.split()
    sen_uni_p = unigram_p[0]
    sen_bi_p = unigram_p[0]
    sen_bik_p = unigram_p[0]

    ### Start your implementation here
    pass

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
    sen_uni_p, sen_bi_p, sen_bik_p = infer(sen1, unigram_p, bi_p, bi_p_k, dict_word2index)

    ### save the probability result into a text file named prob_result.txt,  following the format below
    # sen1, sen_uni_p, sen_bi_p, sen_bik_p
    # sen2, sen_uni_p, sen_bi_p, sen_bik_p

    ### In the same txt file (prob_result.txt), answer the following question:
    # The current corpus contains essays written by second language learners, if the n-grams
    # are trained using essays by native speakers, how would you expect the probability of
    # each sentence change and why?