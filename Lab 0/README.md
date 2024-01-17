

# Text Normalization Project

This project includes a Python script for normalizing text files. It performs various operations like converting text to lowercase, lemmatizing words, removing punctuation, numbers, and stopwords. Additionally, it can plot word frequency distributions.

## Prerequisites

Before running the script, you need to have Python installed on your system. You also need to install the Natural Language Toolkit (NLTK) and Matplotlib for Python. Follow the instructions below to install these packages.

### Installing NLTK

To install NLTK, run one of the following commands in your terminal:

```bash
python3 -m pip install nltk
```


To verify the installation, use:

```bash
python3 -m pip show nltk
```

### Installing Matplotlib

Matplotlib is required for plotting word frequency distributions. Install it using the following command:

```bash
python3 -m pip install matplotlib
```

## Usage

To normalize a text file, use the `normalize_text.py` script followed by the file name and the desired normalization options. Here are some examples of how to use the script:

### Basic Text Normalization

```bash
python3 normalize_text.py Archeological_Investigations.txt --lower --lemmatize --remove_punct --remove_numbers --remove_stopwords
```


### Advanced Usage

For visualizing word frequencies in the text:

```bash
python3 normalize_text.py Tales_of_the_Jazz_Age.txt --lower --lemmatize --remove_punct --remove_numbers --remove_stopwords --plot
```




