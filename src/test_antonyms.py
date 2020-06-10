# test_antonyms.py


# imports
# first time - use first two lines only - then after use third only
#import nltk
#nltk.download('wordnet')
from nltk.corpus import wordnet
from typing import List


antonyms:List[str] = []


def replace(word:str = 'increase') -> None:
    # select list of antonyms for word
    antonyms = []
    for syn in wordnet.synsets(word):
        for lm in syn.lemmas():
            if lm.antonyms():
                antonyms.append(lm.antonyms()[0].name())

    # filter list of antonyms to exclude underscored and hyphented words 
    antonyms = [w for w in antonyms if '_' not in w]
    antonyms = [w for w in antonyms if '-' not in w]

    print('\nset of antonyms of ' + word + ' = ' + str(set(antonyms)))



if __name__ == "__main__": 
    print("test_antonyms module running in diagnostics mode as __main__")
    replace()
else:
    print("test_antonyms module imported")

