'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''
'''
Approach:
An absolutely beautiful data structure. The prefix tree. And also the suffix tree(trie).
One which has intimidated me, but now I truly understand how it works.
Initialize the root as an empty hash table.
For the given string, check if the hash table contains the first letter. If it doesnt add the letter to the hash table, and have the value as another empty hash table. Move to the inner value.... Conitue the same process till the end of the string is reached.

The code is much simpler to understand. Actually constructing the tree makes it much easier.

'''


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.endSymbol = '*'
        
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        #Time O(n) Space : O(n)
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True    
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # Time : O(n) Space : O(1)
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node
        
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
         # Time : O(n) Space : O(1)
        node = self.root
        for letter in prefix:
            if letter not in node:
                return False
            node = node[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
