from .utils import clean_text

def count_words(text):
    words = clean_text(text).split()
    word_count = len(words)
    return word_count

def word_frequencies(text):
    words = clean_text(text).split()
    frequencies = {}
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return frequencies
