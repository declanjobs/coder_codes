

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:

        return self.dfs(self.trie, word)


    def dfs(self, node, word):

        if not len(word):
            return True if node.isEnd else False

        ret = False
        if word[0] == ".":
            for n in node.children.values():
                ret |= self.dfs(n, word[1:])
                if ret:
                    break
        else:
            if word[0] in node.children:
                node = node.children[word[0]]
                ret = self.dfs(node, word[1:])
            else:
                ret = False

        return ret