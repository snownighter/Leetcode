class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        return self.search_helper(word, self.root)

    def search_helper(self, word: str, node: TrieNode) -> bool:
        if not word:
            return node.is_end
        char = word[0]
        if char == '.':
            for child in node.children.values():
                if self.search_helper(word[1:], child):
                    return True
            return False
        else:
            if char in node.children:
                return self.search_helper(word[1:], node.children[char])
            else:
                return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
