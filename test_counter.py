import unittest
from word_counter.counter import count_words, word_frequencies

class TestWordCounter(unittest.TestCase):
    def test_count_words(self):
        text = "Hello world! Hello everyone."
        self.assertEqual(count_words(text), 4)

    def test_word_frequencies(self):
        text = "Hello world! Hello everyone."
        expected_frequencies = {'hello': 2, 'world': 1, 'everyone': 1}
        self.assertEqual(word_frequencies(text), expected_frequencies)

if __name__ == '__main__':
    unittest.main()
