# Importing Libraries
import pandas as pd
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from numpy import dot
from numpy.linalg import norm
from glove import Corpus, Glove

# Function for Training Word2Vec
def train_word2vec(sentences, vector_size=100, window=5, sg=1, min_count=5):
    model = Word2Vec(sentences, vector_size=vector_size, window=window, sg=sg, min_count=min_count)
    return model

# Function for Cosine Similarity
def cosine_similarity(vec1, vec2):
    return dot(vec1, vec2) / (norm(vec1) * norm(vec2))

# Load Dataset
try:
    span_corp = pd.read_csv('corpus.csv')
    assert 'text' in span_corp.columns, "Column 'text' not found in dataset!"
    print("Data loaded successfully!")
except Exception as e:
    print(f"Error loading data: {e}")

# Tokenize sentences (placeholder)
span_corp['tokenized'] = span_corp['text'].str.split()
sentences = span_corp['tokenized'].tolist()

# Query gendered terms
gendered_terms = ["hombre", "mujer", "señor", "señora"]
corp_extracted = span_corp[span_corp['text'].str.contains('|'.join(gendered_terms))]

# Train Word2Vec Model
model = train_word2vec(sentences, vector_size=100, window=5, sg=1, min_count=5)
print("Word2Vec model trained successfully!")

# Train Skipgram Negative Sampling model
embedding_size = 300
window_size = 5
min_word_count = 5
negative_samples = 10

# Define corpus file path for Skipgram model
corpus_file = 'processed_texts.txt'

print("Training Skipgram Negative Sampling model...")
sg_model = Word2Vec(
    sentences=LineSentence(corpus_file),
    vector_size=embedding_size,
    window=window_size,
    min_count=min_word_count,
    sg=1,
    negative=negative_samples,
    workers=4
)

# Save the trained model
sg_model.save("skipgram_model.w2v")
print("Skipgram Negative Sampling model training complete.")

# Load and train GloVe model
corpus = Corpus()
print("Building co-occurrence matrix...")
with open(corpus_file, "r") as f:
    sentences = [line.strip().split() for line in f]
    corpus.fit(sentences, window=10)

print("Training GloVe model...")
glove = Glove(no_components=300, learning_rate=0.05)
glove.fit(corpus.matrix, epochs=50, no_threads=4, verbose=True)
glove.add_dictionary(corpus.dictionary)

# Save the GloVe model
glove.save("glove_model.pkl")
print("GloVe model training complete.")

# Example: Check similarity between two words using Word2Vec
word1, word2 = 'hombre', 'mujer'
similarity = cosine_similarity(model.wv[word1], model.wv[word2])
print(f"Cosine similarity between '{word1}' and '{word2}': {similarity:.4f}")

# Example: Check similarity between words using Skipgram model
similarity_1 = cosine_similarity(sg_model.wv[word1], sg_model.wv[word2])
print(f"Similarity ({word1}, {word2}): {similarity_1}")

# Example: Check similarity using GloVe model
similarity_2 = cosine_similarity(glove.word_vectors[glove.dictionary[word1]],
                                 glove.word_vectors[glove.dictionary[word2]])
print(f"Similarity ({word1}, {word2}): {similarity_2}")

# Query Type Noun Constructions
tn_terms = ["tipo", "clase", "género"]
tn_instances = span_corp[span_corp['text'].str.contains('|'.join(tn_terms))]

# Plot frequency of terms over time
time_periods = [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]  # Example data
frequencies = [10, 20, 15, 25, 30, 28, 35, 40]  # Example data

plt.plot(time_periods, frequencies, marker='o', label="Frequency")
plt.xlabel("Time Periods")
plt.ylabel("Frequency")
plt.title("Frequency of Gendered Terms Over Time")
plt.legend()
plt.grid(True)
plt.show()

# Example: Visualize with PCA
words = ['hombre', 'mujer', 'niño', 'niña', 'padre', 'madre']
vectors = [model.wv[word] for word in words if word in model.wv]

pca = PCA(n_components=2)
reduced_vectors = pca.fit_transform(vectors)

plt.figure(figsize=(8, 6))
for word, vec in zip(words, reduced_vectors):
    plt.scatter(vec[0], vec[1])
    plt.text(vec[0] + 0.02, vec[1], word, fontsize=12)
plt.title("PCA Visualization of Word Embeddings")
plt.show()
