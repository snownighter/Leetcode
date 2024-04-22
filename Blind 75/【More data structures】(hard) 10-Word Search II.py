class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        if not board or not words:
            return []
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        m, n = len(board), len(board[0])
        result = set()
        
        def dfs(i, j, path, node):
            if node.is_end:
                result.add(path)
            
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == '#':
                return
            
            char = board[i][j]
            if char not in node.children:
                return
            
            board[i][j] = '#'
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + dx, j + dy
                dfs(x, y, path + char, node.children[char])
            board[i][j] = char
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, '', trie.root)
        
        return list(result)

        '''
        if not board or not words:
            return []
        
        m, n = len(board), len(board[0])
        result = set()
        
        def dfs(i, j, path, word):
            if not word:
                result.add(path)
                return
            
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == '#':
                return
            
            if board[i][j] != word[0]:
                return
            
            char = board[i][j]
            board[i][j] = '#'
            dfs(i + 1, j, path + char, word[1:])
            dfs(i - 1, j, path + char, word[1:])
            dfs(i, j + 1, path + char, word[1:])
            dfs(i, j - 1, path + char, word[1:])
            board[i][j] = char
        
        for word in words:
            for i in range(m):
                for j in range(n):
                    dfs(i, j, '', word)
        
        return list(result)
        '''
