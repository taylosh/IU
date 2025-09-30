"""
LING545 A0: Basic Text Processing
@author: taylosh
    Open the file specified by the input,
    and split the text into individual words.
    Count the frequency of each word,
    and save the results to the output file.
    The output file should follow this format:
    
    Young   1
    people  3
    ...
"""
import collections

def word_freq(input, output):
    # Read file
    with open(input, 'r', encoding='utf-8') as file:
        text = file.read()
        
    # Force all letters to lowercase and split into words for frquency counts
    words = text.split()
    # Cut non-words
    words = [word for word in words]
    
    # Count the frequency of each
    word_counts = collections.Counter(words)
    
    # Write the results file
    with open(output, 'w', encoding='utf-8') as file:
        for word, count in word_counts.items():
            file.write(f"{word}\t{count}\n")

if __name__ == '__main__':
    input = "ets_sample_l2_writing.txt"
    output = "word_freq.txt"
    word_freq(input, output)
