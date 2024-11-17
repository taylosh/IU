#!/usr/bin/env python3
"""
LING545/CS659 A0.5: Tokenization
@author: Shuju Shi
"""
############################
# In this assignment, you will implement tokenization at the word and sentence level with and without using the
# NLTK package.

### import the libraries
import re
import nltk
import os
import glob

from nltk.tokenize import sent_tokenize, word_tokenize

def tokenization_nltk(input_dir, output_dir_nltk):
    '''
    Use a loop function to read all *.txt files from the directory specified by input_dir,
    perform segmentation at the sentence level and then word level using nltk.
    The library and functions needed from nltk has already been imported for you.
    Write the segmented results into a file, each sentence per line,
    and save it to the directory specified as output_dir_nltk with their original file names.

    The file after tokenization should look like this:

    The result is they do n't spend much time with their community .
    '''

    pass


def tokenization_re(input_dir, output_dir_re):
    '''
    Do the same thing as explained in the tokenization_nltk() function,
    but this time using regular expressions(re).

    Make sure you treat the punctuations such as [,.?!";:'] as words.
    See if you can also handle clitics:
    doesn't -> does n't
    they're -> they 're
    family's -> family 's
    I've -> I 've
    I'd -> I 'd
    We'll -> We 'll

    You may want to refer to the Python documentation on using re.split().
    '''

    pass



if __name__ == "__main__":
    input_dir = "./raw_text"
    output_dir_nltk = "tokenization_nltk"
    output_dir_re = "tokenization_re"

    ### make the output directories
    if not os.path.exists(output_dir_nltk):
        os.makedirs(output_dir_nltk)
    if not os.path.exists(output_dir_re):
        os.makedirs(output_dir_re)


    tokenization_re(input_dir, output_dir_re)
    tokenization_nltk(input_dir, output_dir_nltk)
