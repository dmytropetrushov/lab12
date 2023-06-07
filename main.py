import nltk
import matplotlib.pyplot as plt
from nltk import Text
from nltk.probability import FreqDist

# Downloading the text file
nltk.download('gutenberg')
hamlet_text = nltk.corpus.gutenberg.raw('shakespeare-hamlet.txt')

# Counting the occurrences of 'Hamlet'
hamlet_words = nltk.word_tokenize(hamlet_text)
text = Text(hamlet_words)
hamlet_count = text.count('Hamlet')
print("Occurrences of 'Hamlet':", hamlet_count)

# Finding common context
text.concordance('Hamlet')
text.concordance('Horatio')

# Plotting the distribution of selected words
words_of_interest = ['Hamlet', 'Horatio', 'Ghost', 'Polonius']
fdist = FreqDist(hamlet_words)

# Counting unique tokens
unique_tokens = set(hamlet_words)
num_unique_tokens = len(unique_tokens)
print("Number of unique tokens:", num_unique_tokens)

# Showing words that occur only once
single_occurrence_words = [word for word, frequency in fdist.items() if frequency == 1]
print("Words occurring only once:", single_occurrence_words)

# Comparing word lists
long_words = [word for word, frequency in fdist.items() if len(word) > 7 and frequency > 7]
short_words = [word for word, frequency in fdist.items() if len(word) < 3 and frequency < 3]

print("Long words (length > 7, frequency > 7):", long_words)
print("Short words (length < 3, frequency < 3):", short_words)

# Lexical richness function
def lexical_richness(text):
    num_words = len(text)
    num_unique_words = len(set(text))
    return num_words / num_unique_words

richness = lexical_richness(hamlet_words)
print("Lexical richness:", richness)

# Probability function
def word_probability(word, corpus_size):
    return fdist[word] / corpus_size

word = "Hamlet"
corpus_size = len(hamlet_words)
probability = word_probability(word, corpus_size)
print("Probability of", word, "appearing:", probability)

# Collocations
text.collocations()

# Long words
long_words = [word for word in hamlet_words if len(word) > 12]
print("Words longer than 12 characters:", long_words)

# Distribution of word lengths
word_lengths = [len(word) for word in hamlet_words]
length_dist = FreqDist(word_lengths)

# Most frequent word length
most_common_length = length_dist.max()
frequency = length_dist[most_common_length]
print("Most frequent word length:", most_common_length)
print("Frequency:", frequency)

# Word lengths in the corpus
lengths = length_dist.keys()
print("Word lengths in the corpus:", lengths)

# Displaying word lengths with frequencies
for length, frequency in length_dist.items():
    print("Length:", length, "- Frequency:", frequency)
