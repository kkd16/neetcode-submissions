class PrefixTree:

    class PrefixNode:
        def __init__(self):
            self.children = {}
            self.end = False

    def __init__(self):
        self.root = self.PrefixNode()
        

    def insert(self, word: str) -> None:

        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = self.PrefixNode()
            cur = cur.children[c]

        cur.end = True


    def search(self, word: str) -> bool:

        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.end
        

    def startsWith(self, prefix: str) -> bool:

        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True
        
        