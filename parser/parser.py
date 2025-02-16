import nltk
import sys
import re
from collections import deque

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP
S -> NP VP NP
S -> NP VP NP VP
S -> NP VP Adv Conj VP
S -> NP VP NP Conj VP NP
S -> NP VP NP NP NP

NP -> N | Det N
NP -> Det N | Det Adj N
NP -> P N | P Det N
NP -> P Det Adj N | P Det N Adv
NP -> Conj N | Adj N
NP -> N | N Adv
VP -> V | V NP
"""


grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    words = nltk.word_tokenize(sentence)
    return [word.lower() for word in words if re.search(r"[a-zA-Z]", word)]


def np_chunk(tree):
    """
    Return a list of noun phrase chunks in the sentence tree.
    A noun phrase chunk is a subtree whose label is NP and that does not itself
    contain other noun phrases.
    """
    np_chunks = []

    # Traverse all subtrees
    for subtree in tree.subtrees():
        if subtree.label() == "NP":
            # Ensure this NP doesn't contain another NP inside it (DFS)
            stack = deque(subtree)  # Stack stores child nodes

            contains_np = False  # Flag to check if a nested NP exists

            while stack:
                node = stack.pop()  # Get the next node
                if isinstance(node, nltk.Tree):  # Ensure node is a subtree
                    if node.label() == "NP":
                        contains_np = True
                        break  # Found nested NP, no need to process further
                    stack.extend(node)  # Add children to stack

            if not contains_np:
                np_chunks.append(subtree)  # Add subtree if it's an NP chunk

    return np_chunks


if __name__ == "__main__":
    main()
