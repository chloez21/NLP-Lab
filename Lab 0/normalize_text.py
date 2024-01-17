import sys
import argparse
from collections import Counter
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

# Download necessary NLTK data
nltk.download('punkt') # work with tokenizer
nltk.download('wordnet')  # work with lemmatizer
nltk.download('stopwords')

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str)
    parser.add_argument('--lower', action='store_true')
    parser.add_argument('--stem', action='store_true')
    parser.add_argument('--lemmatize', action='store_true')
    parser.add_argument('--remove_stopwords', action='store_true')
    parser.add_argument('--remove_punct', action='store_true')
    parser.add_argument('--remove_numbers', action='store_true')
    parser.add_argument('--plot', action='store_true')
    return parser


def normalize_text(file_path, lower, stem, lemmatize, remove_stopwords, remove_punct,remove_numbers, plot):
    # Load the file
    with open(file_path, 'r') as file:
        text = file.read()

    # Tokenize text
    tokens = nltk.word_tokenize(text)

    if lower:
        tokens = [token.lower() for token in tokens]

    # Initialize stemmer and lemmatizer
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    if stem:
        tokens = [stemmer.stem(token) for token in tokens]

    if lemmatize:
        tokens = [lemmatizer.lemmatize(token) for token in tokens]

    if remove_stopwords:
        sw = set(stopwords.words('english'))
        # print(sw)
        #tokens = [token for token in tokens if token not in sw]
        # keep stopwords
        tokens = [token for token in tokens if token in sw]

    if remove_punct:
        tokens = [token for token in tokens if token.isalpha()]

    if remove_numbers:
        tokens = [token for token in tokens if not token.isdigit()]


    # Count and sort tokens
    token_count = Counter(tokens)

    if plot:
        plot_counts(token_count.most_common())

    return token_count.most_common() #  Counter('abcdeabcdabcaba')=>[('a', 5), ('b', 4), ('c', 3)]

def plot_counts(sorted_tokens):

    words, freqs = zip(*sorted_tokens)
    ranks = range(1, len(words) + 1)

    plt.figure(figsize=(10, 6))

    plt.plot(ranks, freqs, marker='o')  # line plot
    # plt.bar(ranks, freqs)  # bar plot

    # set the log scale
    plt.xscale('log')
    plt.yscale('log')

    # retrive file's name
    file_name = sys.argv[1].split('/')[-1]
    plt.title('Word Frequencies of ' + file_name)
    plt.xlabel('Rank')
    plt.ylabel('Frequency')

    plt.show()

def main():
    parser = create_parser()
    args = parser.parse_args()

    # Normalize the text
    counts = normalize_text(args.file, args.lower, args.stem, args.lemmatize, args.remove_stopwords, args.remove_punct, args.remove_numbers, args.plot)
    # print(counts)

    for word, count in counts:
        print(f"{word} {count}")


if __name__ == "__main__":
    main()
