# MillionGazillion
# ---------------- # 

# I'm making a search engine called
# MillionGazillionTM.
# I wrote a crawler that visits web pages, stores a few keywords in a database, and
# follows links to other web pages. I noticed that my crawler was wasting a lot of time
# visiting the same pages over and over, so I made a set, visited, where I'm storing
# URLs I've already visited. Now the crawler only visits a URL if it hasn't already been
# visited.
# Thing is, the crawler is running on my old desktop computer in my parents' basement
# (where I totally don't live anymore), and it keeps running out of memory because
# visited is getting so huge.
# How can I trim down the amount of space taken up by visited?

class Trie(object):
    def __init__(self):
        
        # self.root_note is dictionary
        self.root_node = {}
    
    def add_word(self, word):
        current_node = self.root_node
        is_new_word = False

        # Work downwards through the trie, adding nodes as 
        # needed, and keep track of whether we add any nodes. 

        for char in word:
            if char not in current_node:
                is_new_word = True
                current_node[char] = {}
            
            # when char is present in current_node
            current_node = current_node[char]

        # Explicitly mark the end of a word
        # Otherwise, we might say a word is present
        # if it is a prefix of a different longer word that was 
        # added earlier

        if "End Of Word" not in current_node:
            is_new_word = True
            current_node["End Of Word"] = {}

        return is_new_word

# For this problem we can also use ternary search tree as well. 
# A bloom filter also works - specialy if you use run-length 
# encoding

# Complexity 
#------------#
# - For simplicity, lets assume we will be only using 26 english 
# characters (lowercase) to build url. If we had used hashset
# then our space complexity will be O(n 26^n ). 
# - Using trie, the space is reduced by n factor. So it will be
# O(26^n)


