# Importing nltk and shuffle form random for tokenization, ngrams, shuffle, and frequency distribution functions
import nltk
from random import shuffle

"""

1. Simulating a Dataset

"""

# Reading text files to variables
file = open("./genesis.txt", encoding="utf8")
genesis = file.read()
file.close()
file = open("./alice_in_wonderland.txt", encoding="utf8")
alice = file.read()
file.close()
file = open("./wizard_of_oz.txt", encoding="utf8")
wizard = file.read()
file.close()
file = open("./J. K. Rowling - Harry Potter 1 - Sorcerer's Stone.txt")
harry1 = file.read()
file.close()
file = open("./J. K. Rowling - Harry Potter 2 - The Chamber Of Secrets.txt")
harry2 = file.read()
file.close()
file = open("./J. K. Rowling - Harry Potter 3 - Prisoner of Azkaban.txt")
harry3 = file.read()
file.close()
file = open("./J. K. Rowling - Harry Potter 4 - The Goblet of Fire.txt")
harry4 = file.read()
file.close()

# Tokenizing into list of words
genesis = nltk.word_tokenize(genesis)
alice = nltk.word_tokenize(alice)
wizard = nltk.word_tokenize(wizard)
harry1 = nltk.word_tokenize(harry1)
harry2 = nltk.word_tokenize(harry2)
harry3 = nltk.word_tokenize(harry3)
harry4 = nltk.word_tokenize(harry4)

# Making 3-shingles of words in the documents
genesis = set(list(nltk.ngrams(genesis, 3)))
alice = set(list(nltk.ngrams(alice, 3)))
wizard = set(list(nltk.ngrams(wizard, 3)))
harry1 = set(list(nltk.ngrams(harry1, 3)))
harry2 = set(list(nltk.ngrams(harry2, 3)))
harry3 = set(list(nltk.ngrams(harry3, 3)))
harry4 = set(list(nltk.ngrams(harry4, 3)))
harry4copy = set(list(nltk.ngrams(harry4, 3)))

documents = [genesis,alice,wizard,harry2,harry2,harry3,harry4]

"""

2. Minhashing

"""
# setting the vocab as the union of all documents
"""
def setVocab(documents):
    vocab = []
    for doc in documents:
        vocab.union(doc)
    return vocab

vocab = setVocab(documents)
"""
vocab = genesis.union(alice).union(wizard).union(harry1).union(harry2).union(harry3).union(harry4)

# generating the one-hots
"""
def oneHot(docs):
    oneHots = []
    for doc in docs:
        oneHots.append([1 if x in doc else 0 for x in vocab])
    return oneHots

oneHots = oneHot(documents)
"""

genesis_hot = [1 if x in genesis else 0 for x in vocab]
alice_hot = [1 if x in alice else 0 for x in vocab]
wizard_hot = [1 if x in wizard else 0 for x in vocab]
harry1_hot = [1 if x in harry1 else 0 for x in vocab]
harry2_hot = [1 if x in harry2 else 0 for x in vocab]
harry3_hot = [1 if x in harry3 else 0 for x in vocab]
harry4_hot = [1 if x in harry4 else 0 for x in vocab]

# psuedo random number list
def createHash():
    hash_ex = list(range(1,len(vocab)+1))
    shuffle(hash_ex)
    return hash_ex

# creating array of minhashes
def minHashList(size):
    hashes = []
    for _ in range(size):
        hashes.append(createHash())
    return hashes

# taking the one-hots and creating the signatures
def hash(vectors):
    sig = []
    for x in minHashes:
        for i in range(1, len(vocab)+1):
            if vectors[x[i]] == 1:
                sig.append(x[i])
                break
    return sig

# getting the minhash list
minHashes = minHashList(100)

# generating the signatures for each document
"""
def sig(hots):
    sigs = []
    for hot in hots:
        sigs.append(hash(hot))
    return sigs

sigs = sig(oneHots)
"""

genesis_sig = hash(genesis_hot)
alice_sig = hash(alice_hot)
wizard_sig = hash(wizard_hot)
harry1_sig = hash(harry1_hot)
harry2_sig = hash(harry2_hot)
harry3_sig = hash(harry3_hot)
harry4_sig = hash(harry4_hot)
harry4copy_sig = hash(harry4_hot)


# jaccard function
def jaccard(x, y):
    return len(set(x).intersection(y)) / len(set(x).union(y))

"""
# combiniations for jaccard function
def combinations(array, function):
    funcArray = []
    for i in range(0, len(array)-1):
        for j in range(1,len(array)):
            if(i == j):
                continue
            funcArray.append(function(array[i,j]))
    return funcArray

# getting jaccard similarities of each document pair
jacSims = combinations(sigs,jaccard)

print(jacSims[0])

"""
"""
a_g = jaccard(set(alice_sig), set(genesis_sig))
w_g = jaccard(set(wizard_sig), set(genesis_sig))
h1_g = jaccard(set(harry1_sig), set(genesis_sig))
h2_g = jaccard(set(harry2_sig), set(genesis_sig))
h3_g = jaccard(set(harry3_sig), set(genesis_sig))
h4_g = jaccard(set(harry4_sig), set(genesis_sig))
h4c_g = jaccard(set(harry4copy_sig), set(genesis_sig))
w_a = jaccard(set(wizard_sig), set(alice_sig))
h1_a = jaccard(set(harry1_sig), set(alice_sig))
h2_a = jaccard(set(harry2_sig), set(alice_sig))
h3_a = jaccard(set(harry3_sig), set(alice_sig))
h4_a = jaccard(set(harry4_sig), set(alice_sig))
h4c_a = jaccard(set(harry4copy_sig), set(alice_sig))
h1_w = jaccard(set(harry1_sig), set(wizard_sig))
h2_w = jaccard(set(harry2_sig), set(wizard_sig))
h3_w = jaccard(set(harry3_sig), set(wizard_sig))
h4_w = jaccard(set(harry4_sig), set(wizard_sig))
h4c_w = jaccard(set(harry4copy_sig), set(wizard_sig))
h2_h1 = jaccard(set(harry2_sig), set(harry1_sig))
h3_h1 = jaccard(set(harry3_sig), set(harry1_sig))
h4_h1 = jaccard(set(harry4_sig), set(harry1_sig))
h4c_h1 = jaccard(set(harry4copy_sig), set(harry1_sig))
h3_h2 = jaccard(set(harry3_sig), set(harry2_sig))
h4_h2 = jaccard(set(harry4_sig), set(harry2_sig))
h4copy_h2 = jaccard(set(harry4copy_sig), set(harry2_sig))
h4_h3 = jaccard(set(harry4_sig), set(harry3_sig))
h4copy_h3 = jaccard(set(harry4copy_sig), set(harry3_sig))
h4c_h4 = jaccard(set(harry4copy_sig), set(harry4_sig))
"""


"""

3. Locality-Sensitive Hashing 

"""
"""
def splitVector(sigs, x):
    rows = int(len(sig)/x)
    subVectors = []
    for sig in sigs:
        for i in range(0, len(sig), rows):
            subVectors.append(sig[i : i + rows])
        return subVectors

bands = splitVector(sigs)
"""

# splitting vector function
def splitVector(sig, x):
    rows = int(len(sig)/x)
    subVectors = []
    for i in range(0, len(sig), rows):
        subVectors.append(sig[i : i + rows])
    return subVectors

# splitting signatures into bands of signatures

genesis_band = splitVector(genesis_sig, 50)
alice_band = splitVector(alice_sig, 50)
wizard_band = splitVector(wizard_sig, 50)
harry1_band = splitVector(harry1_sig, 50)
harry2_band = splitVector(harry2_sig, 50)
harry3_band = splitVector(harry3_sig, 50)
harry4_band = splitVector(harry4_sig, 50)
harry4copy_band = splitVector(harry4copy_sig, 50)


"""

4. Similarity Estimation

"""

# matching bands of signitures between documents
"""
def canididatePair(bands):
    paris = []
    for band1,band2 in bands:
        for rows1, rows2 in zip(band1, band2):
            if rows1 == rows2:
                pairs.append((band1,band2))
                break

pairs = canididatePair(bands)
print(pairs)
"""
def candidatePair(band1, band2):
    for rows1, rows2 in zip(band1, band2):
        if rows1 == rows2:
            return True
        

if candidatePair(harry1_band,harry3_band):
    print("harry1 and harry3 jaccard similarity is: ", jaccard(harry1_sig,harry3_sig))
else:
    print("harry1 and harry3 are not similar")

if candidatePair(harry4_band,harry4copy_band):
    print("harry4 and harry4copy jaccard similarity is: ", jaccard(harry4_sig,harry4copy_sig))
else:
    print("harry4 and harry4copy are not similar")
