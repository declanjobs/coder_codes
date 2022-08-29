class Trie:

    def __init__(self):
        self.children = {}
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self

        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.startsWith(word)
        return True if node and node.isEnd else False

    def startsWith(self, prefix: str) -> bool:
        node = self

        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return None

        return node

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)