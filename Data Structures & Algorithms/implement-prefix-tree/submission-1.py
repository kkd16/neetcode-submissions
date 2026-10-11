class PrefixTree:

    class Node:
        def __init__(self):
            self.children = {}
            self.end = False

    # make an n-ary tree
    # have a root node that points to a series of nodes
    # each node has 1 letter and a true/false end of word
    # end of word does not restrict it from having children it just
    # signifies that there is a word ending here 
    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = self.Node()
                curr = curr.children[c]
        
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return True
        
        