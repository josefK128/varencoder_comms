# test_synonyms.py


# imports
# first time - use first two lines only - then after use third only
#import nltk
#nltk.download('wordnet')
from nltk.corpus import wordnet
from typing import List


synonyms:List[str] = []


def replace(word:str = 'travel') -> None:
    # select list of synonyms for word
    synonyms = []
    for syn in wordnet.synsets(word):
        for lm in syn.lemmas():
            synonyms.append(lm.name())

    # filter list of synonyms to exclude underscored and hyphented words 
    synonyms = [w for w in synonyms if '_' not in w]
    synonyms = [w for w in synonyms if '-' not in w]

    print('\nset of synonyms of ' + word + ' = ' + str(set(synonyms)))



if __name__ == "__main__": 
    print("test_synonyms module running in diagnostics mode as __main__")
    replace('car')
else:
    print("test_synonyms module imported")

