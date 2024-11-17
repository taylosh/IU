"""
LING545/CS659 A0.5: Tokenization
@author: taylosh
    
Two functions for sentence & word segmentation of essays
    tokenization_nltk(): nltk sent_tokenize & word_tokenize functions
    tokenization_re(): regex defined custom patterns

Each takes input directory, segments text, and writes tokenized results to output
file directories
"""
### import the libraries
import re
import nltk
import os
import glob

from nltk.tokenize import sent_tokenize, word_tokenize

def tokenization_nltk(input_dir, output_dir_nltk):
    # Loop files in input dir
    for file_path in glob.glob(os.path.join(input_dir, "*.txt")):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Sentence tokenize
        sents = sent_tokenize(text)
        
        # Word tokenize within sentence
        tok_sents = [" ".join(word_tokenize(sent)) for sent in sents]
        
        # Output file path
        output_file_path = os.path.join(output_dir_nltk, os.path.basename(file_path))
        
        # Write tokenized sentences to output
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for sent in tok_sents:
                output_file.write(sent + '\n')


def tokenization_re(input_dir, output_dir_re):
    # Define regex pattern for word tok
    # Word boundaries + potential punctuation
    word_pattern = r"\b[\w']+\b|[.,!?;\"':]"
    
    # Loop files in input dir
    for file_path in glob.glob(os.path.join(input_dir, "*.txt")):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Sentence tokenize by basic split on '.', '?', and '!'
        sents = re.split(r'(?<=[.!?]) +', text)
        
        # Word tokenization using the defined regular expression pattern
        tok_sents = [" ".join(re.findall(word_pattern, sent)) for sent in sents]
        
        # Output file path
        output_file_path = os.path.join(output_dir_re, os.path.basename(file_path))
        
        # Write tokenized sentences to output
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for sent in tok_sents:
                output_file.write(sent + '\n')



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