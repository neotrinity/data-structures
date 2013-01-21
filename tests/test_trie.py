import os
import sys
import unittest
import random

sys.path.append(os.path.join(r'..', 'src'))

from trie import Trie

class TestTrie(unittest.TestCase):
    
    def setUp(self):
        self.trie = Trie()
        self.words = ['goings', 'poodle', 'goose', 'porky', 'pottery', 'zebra']
        self.word = random.choice(self.words)

        
    def test_add(self):
        t = self.trie
        word = self.word
        dummy_word = 'XXXDUMMYXXX'
        t.add(word)
        self.assertTrue(t.find(word))
        self.assertFalse(t.find(dummy_word))

    def test_add_with_payload(self):
        t = self.trie
        word = self.word
        dummy_payload = 10
        t.add(word, 10)
        self.assertEquals(t.find(word), dummy_payload)

    def test_incomplete_word(self):
        t = self.trie
        for word in self.words:
            t.add(word)
        incomplete_word = 'going'
        self.assertFalse(t.find(incomplete_word))
        
    def test_remove(self):
        t = self.trie
        for word in self.words:
            t.add(word)
        word = 'porky'
        t.remove(word)
        self.assertFalse(t.find(word))
        word = 'goose'
        t.remove(word)
        self.assertFalse(t.find(word))
        word = 'cola'
        t.remove(word)
        self.assertFalse(t.find(word))

    def test_remove_word_not_found(self):
         t = self.trie
         word = self.word
         dummy_word = word[:-1]

         t.add(word)
         t.remove(dummy_word)
         self.assertTrue(t.find(word))

    def test_showWords(self):
        t = self.trie
        for word in self.words:
            t.add(word)
        self.assertEquals(set(t.showWords()), set(self.words))
        

    def test_autocomplete(self):
        t = self.trie
        prefix = self.word[:2]
        prefix_words = [ w for w in self.words if w.startswith(prefix) ]

        for word in self.words:
            t.add(word)
        self.assertEquals(set(t.autocomplete(prefix)), set(prefix_words))

        self.assertEquals(t.autocomplete('qqqq'), None)

    def test_empty_trie(self):
        t = self.trie
        self.assertEquals(set(t.showWords()), set([]))

if __name__ == '__main__':
    unittest.main()
