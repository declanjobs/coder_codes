from typing import List

class Trie:
    def __init__(self):
        # do initialization if necessary
        self.children = [None] * 26
        self.isEnd = False

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
             we will sort your return value in output
    """
    def word_search_i_i(self, board: List[List[str]], words: List[str]) -> List[str]:
        # write your code here
        from collections import deque

        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        m = len(board)
        if not m:
            return []
        n = len(board[0])

        trie = Trie()

        for w in words:
            trie.insert(w)

        ans = set()
        visited = set()

        def dfs(i, j, node, w):

            visited.add((i,j))
            w += board[i][j]
            node = node.children[ord(board[i][j])-ord("a")]

            if node and node.isEnd:
                ans.add(w)

            for d in directions:
                ii, jj = i+d[0], j+d[1]
                if 0<=ii<m and 0<=jj<n and (ii,jj) not in visited and node:
                    dfs(ii,jj,node,w)

            visited.remove((i,j))

        for i in range(m):
            for j in range(n):
                dfs(i,j,trie,"")

        return list(ans)