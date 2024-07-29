import argparse
from word_counter.counter import count_words, word_frequencies

def main():
    parser = argparse.ArgumentParser(description="Word Counter")
    parser.add_argument('file', type=str, help="Path to the text file")
    parser.add_argument('--frequencies', action='store_true', help="Show word frequencies")
    args = parser.parse_args()

    try:
        with open(args.file, 'r') as file:
            text = file.read()
            print(f"Total number of words: {count_words(text)}")
            if args.frequencies:
                freqs = word_frequencies(text)
                for word, freq in freqs.items():
                    print(f"{word}: {freq}")
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")

if __name__ == "__main__":
    main()
