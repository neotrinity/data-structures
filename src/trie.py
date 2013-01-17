import os

class TrieNode(object):
    """
          Trie Node 
    """
    
    def __init__(self,key):
        self._key = key
        self._value = None
        self._children = {}
        self._isWord = False
        
    isWord = property( lambda self: self._isWord,
                       lambda self, value: setattr(self,'_isWord',value),
                       doc = """ Property to get/set _isWord """)
                       
                       
class Trie(object):
    """
         Standard Trie Implementation
    """
    
    def __init__(self):
        self._root = TrieNode("")
        
    def add(self, word, value=None):
        """
            Add word into the trie with an optional payload
        """
        letters = list(word)
        node = self._root
        
        for letter in letters:
            if letter not in node._children:
                node._children[letter] = TrieNode(letter)                
            node = node._children[letter]
            
        node.isWord = True               # Flag the word entry
        node._value = value
        
    def find(self, word):
        """
            Find a given word in the Trie, 
            if payload is present then return the payload
            else return bool for the presence of the word
        """
        letters = list(word)
        node = self._root
        
        for letter in letters:
            if letter not in node._children:
                return False
            node = node._children[letter]
        if node.isWord:
            if node._value:
                return node._value
            else:
                return True
        else:
            return False

    def remove(self, word):
        """
            Remove the word from the Trie
        """
        letters = list(word)
        node = self._root
        leastCommonPrefix = node
        toDel = letters[0]
        
        for letter in letters:
            if letter not in node._children:
                print "%s Not Found" % word
                return None
                
            if len(node._children.keys()) >  1:
                leastCommonPrefix = node
                toDel = letter
            node = node._children[letter]
            
        if node.isWord:
            node = None
            del leastCommonPrefix._children[toDel] # Delete the reference
            leastCommonPrefix = None
            print "Removed %s" % word
            return None
        else:
            print "This search string is NOT a word"
            return None
            
    def showWords(self, fromNode = None, prefix = ""):
        """
            Returns a list of all the words held by the Trie
        """
        if fromNode:
            node = fromNode
        else:
            node = self._root
        words = []
        
        def preOrderTraversal(node,word):
            word += node._key
            if node.isWord:
                words.append(word)               # valid word, add it to the list
            if not node._children:                       # reached the leaf
                word = prefix                            # reset the word with the prefix
            for letter, n in node._children.items():
                preOrderTraversal(n,word)
                
        preOrderTraversal(node,prefix)
        return words
        
    def autocomplete(self,wordPrefix):
        """
            Given a word prefix, this fetches all the words held in the
            Trie which start with the prefix
        """
        letters = list(wordPrefix)
        node = self._root
        
        for letter in letters:
            if letter not in node._children:
                return None
            node = node._children[letter]
        
        return self.showWords(node,wordPrefix[:-1])
        
        
if __name__ == '__main__':
    # Testing the Trie
    
    t = Trie()
    t.add('goose')
    t.add('going')
    t.add('porky')
    t.add('poodle')
    t.add('poker')
    print " Trie is created with the following words "
    print t.showWords()
    
    print "Go : %s" % t.find('go')
    print "porky : %s" % t.find('porky')
    print "poodle : %s" % t.find('poodle')
    t.remove('poodle')
    t.remove('poodle')
    print "poodle : %s" % t.find('poodle')
    print " The following elements are currently in the Trie"
    print t.showWords()

    print " The autocomplete for prefix go are :"
    print t.autocomplete('go')
            
