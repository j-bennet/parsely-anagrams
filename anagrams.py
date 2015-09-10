# -*- coding: utf-8 -*-
from __future__ import print_function
from collections import defaultdict
from random import choice, shuffle, randint


DICTIONARY = open("/usr/share/dict/words")


class AnagramMaster(object):
    """
    Generates anagrams. Uses a set of words to generate anagrams from.
    """

    words = None
    letters = list('abcdefghijklmnopqrstuvwxyz')
    current_word = None

    def __init__(self, words=None):
        """
        Initialize with words.
        :param words: set
        """
        self.words = set(words)

    def generate_anagram_with_difficulty(self, difficulty=1, unsolvable=False):
        """
        Generates one anagrams of a word with given length.
        """
        result = list(self._select_word(difficulty))
        shuffle(result)
        if unsolvable:
            result = self._make_unsolvable(result)
        return result

    def is_correct(self, anagram, answer):
        """
        Verifies if answer to a given anagram is correct.
        :param anagram: list
        :param answer: list
        :return: boolean
        """
        if ''.join(answer) not in self.words:
            return False

        # TODO: not the best way to compare! Simpler way is to sort letters, join into strings, and compare strings.
        letter_count_anagram = self._count_letters(anagram)
        letter_count_answer = self._count_letters(answer)

        return letter_count_anagram == letter_count_answer

    def _count_letters(self, word):
        """
        Count all letters in a word and return a set with tuples.
        :param word: list
        :return: set with tuples (letter, N) where N is count
        """
        result = defaultdict()
        for l in word:
            result.setdefault(l, 1)
            result[l] += 1
        result_set = set([])
        for k, v in result.items():
            result_set.add((k, v))
        return result

    def _make_unsolvable(self, word):
        """
        Take a real anagram and scramble some characters in it.
        :param word: list
        :return: string with some additional chars or chars missing
        """
        chars = list(word)

        # how many chars to replace? maybe add a parameter?
        num_of_chars = len(word) / 5

        for i in range(num_of_chars):
            char_to_replace = randint(0, len(word))
            chars[char_to_replace] = choice(self.letters)

        result = ''.join(chars)

        # If it's in the set of dict words, it's a real word and it's still
        # solvable. Let's try again.
        if result in self.words:
            result = self._make_unsolvable(word)
        return result

    def _select_word(self, word_length):
        """
        Selects a word of a given length from a set.
        """
        words_of_len = [w for w in self.words if len(w) == word_length]
        self.current_word = choice(words_of_len)
        return self.current_word


def read_words():
    """
    Read words from file into a set.
    :return: set
    """
    global DICTIONARY
    words = set([])
    for word in DICTIONARY:
        words.add(word.strip())
    return words


if __name__ == "__main__":
    print("Use the classes from this module.")

    # create a set using filehandle

    words = read_words()
    am = AnagramMaster(words)
