# Importing Libraries
import pandas as pd
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from numpy import dot
from numpy.linalg import norm

# Function for Training Word2Vec
def train_word2vec(sentences, vector_size=100, window=5, sg=1, min_count=5):
    model = Word2Vec(sentences, vector_size=vector_size, window=window, sg=sg, min_count=min_count)
    return model

# Function for Cosine Similarity
def cosine_similarity(model, word1, word2):
    try:
        vec1, vec2 = model.wv[word1], model.wv[word2]
        return dot(vec1, vec2) / (norm(vec1) * norm(vec2))
    except KeyError as e:
        print(f"Word not found in vocabulary: {e}")
        return None

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
print("Model trained successfully!")

# Set up parameters for Skipgram Negative Sampling
embedding_size = 300  # Dimensionality of the word vectors
window_size = 5       # Context window size
min_word_count = 5    # Minimum word count threshold
negative_samples = 10 # Number of negative samples

# Train the Skipgram model
print("Training Skipgram Negative Sampling model...")
sg_model = Word2Vec(
    sentences=LineSentence(corpus_file),
    vector_size=embedding_size,
    window=window_size,
    min_count=min_word_count,
    sg=1,  # Skipgram is specified with sg=1
    negative=negative_samples,
    workers=4  # Number of threads to use
)

# Save the trained model
sg_model.save("skipgram_model.w2v")

print("Skipgram Negative Sampling model training complete.")

# Import necessary libraries for GloVe
from glove import Corpus, Glove

# Load preprocessed corpus
corpus_file = "processed_texts.txt"  # Replace with your actual file

# Step 1: Build the Co-occurrence Matrix
corpus = Corpus()
print("Building co-occurrence matrix...")
with open(corpus_file, "r") as f:
    sentences = [line.strip().split() for line in f]  # Tokenized sentences
    corpus.fit(sentences, window=10)  # Specify context window size

# Step 2: Train GloVe Model
print("Training GloVe model...")
glove = Glove(no_components=300, learning_rate=0.05)  # Set embedding size
glove.fit(corpus.matrix, epochs=50, no_threads=4, verbose=True)  # Train the model
glove.add_dictionary(corpus.dictionary)  # Add vocabulary

# Save the GloVe model
glove.save("glove_model.pkl")

print("GloVe model training complete.")

# Compute Cosine Similarity
word1, word2 = 'hombre', 'mujer'
similarity = cosine_similarity(model, word1, word2)
if similarity is not None:
    print(f"Cosine similarity between '{word1}' and '{word2}': {similarity:.4f}")

# Cosine similarity function
def cosine_similarity(vec1, vec2):
    return dot(vec1, vec2) / (norm(vec1) * norm(vec2))

# Example: Check similarity between two words
word1 = "hombre"  # Male-denoting term
word2 = "poder"   # Associated with power
word3 = "mujer"   # Female-denoting term

# For Skipgram model
similarity_1 = cosine_similarity(sg_model.wv[word1], sg_model.wv[word2])
similarity_2 = cosine_similarity(sg_model.wv[word3], sg_model.wv[word2])

print(f"Similarity ({word1}, {word2}): {similarity_1}")
print(f"Similarity ({word3}, {word2}): {similarity_2}")

# For GloVe model
similarity_3 = cosine_similarity(glove.word_vectors[glove.dictionary[word1]],
                                 glove.word_vectors[glove.dictionary[word2]])
similarity_4 = cosine_similarity(glove.word_vectors[glove.dictionary[word3]],
                                 glove.word_vectors[glove.dictionary[word2]])

print(f"Similarity ({word1}, {word2}): {similarity_3}")
print(f"Similarity ({word3}, {word2}): {similarity_4}")

# Query Type Noun Constructions
tn_terms = ["tipo", "clase", "género"]
tn_instances = span_corp[span_corp['text'].str.contains('|'.join(tn_terms))]

# Plot frequency of terms over time
plt.plot(time_periods, frequencies)
plt.title('Frequency of Gendered Terms Over Time')
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

# Example: Plot Frequency Trends (Dummy Data)
time_periods = [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
frequencies = [10, 20, 15, 25, 30, 28, 35, 40]

plt.plot(time_periods, frequencies, marker='o', label="Frequency")
plt.xlabel("Time Periods")
plt.ylabel("Frequency")
plt.title("Frequency of Gendered Terms Over Time")
plt.legend()
plt.grid(True)
plt.show()
