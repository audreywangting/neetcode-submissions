class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root # start with root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode() # 建立新的child node
            node = node.children[char] # 移動目前的node到下一個char對應的child node
        node.is_end = True
        

    def search(self, word: str) -> bool:
        def dfs(i, node): # i: 現在要匹配的word[i], node: 目前位於trie哪個node
            # 1. base case
            if i == len(word):
                return node.is_end

            # 2. normal char
            char = word[i]

            if char != ".":
                if char not in node.children:
                    return False
                return dfs(i+1, node.children[char]) # 繼續匹配

            # 3. "."
            for child in node.children.values():
                if dfs(i+1, child):
                    return True

            return False

        return dfs(0, self.root)




