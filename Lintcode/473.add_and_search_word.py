class Trie:
    def __init__(self):
        # do initialization if necessary
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def searchPrefix(self, prefix: str) -> "Trie":

        l = len(prefix)

        def dfs(node, idx):
            if idx >= l:
                return node

            s = prefix[idx]

            if s != ".":
                ch = ord(s) - ord("a")
                if not node.children[ch]:
                    return None
                else:
                    return dfs(node.children[ch], idx+1)

            else:
                ret = None
                for child in node.children:
                    if child:
                        ret = dfs(child, idx+1)
                        if ret and ret.isEnd:
                            return ret

                return ret

        return dfs(self, 0)

class WordDictionary:
    def __init__(self):
        self.trie = Trie()

    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def addWord(self, word):
        # write your code here
        self.trie.insert(word)

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # write your code here
        return self.trie.search(word)
