# subst_synonyms.py


# imports
# first time - use first two lines only - then after use third only
#import nltk
#nltk.download('wordnet')
from nltk.corpus import wordnet
import re
from random import randint
from typing import List, Tuple


#stop words list
stop_words:List[str] = ['i', 'me', 'my', 'myself', 'we', 'our', 
			'ours', 'ourselves', 'you', 'your', 'yours', 
			'yourself', 'yourselves', 'he', 'him', 'his', 
			'himself', 'she', 'her', 'hers', 'herself', 
			'it', 'its', 'itself', 'they', 'them', 'their', 
			'theirs', 'themselves', 'what', 'which', 'who', 
			'whom', 'this', 'that', 'these', 'those', 'am', 
			'is', 'are', 'was', 'were', 'be', 'been', 'being', 
			'have', 'has', 'had', 'having', 'do', 'does', 'did',
			'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or',
			'because', 'as', 'until', 'while', 'of', 'at', 
			'by', 'for', 'with', 'about', 'against', 'between',
			'into', 'through', 'during', 'before', 'after', 
			'above', 'below', 'to', 'from', 'up', 'down', 'in',
			'out', 'on', 'off', 'over', 'under', 'again', 
			'further', 'then', 'once', 'here', 'there', 'when', 
			'where', 'why', 'how', 'all', 'any', 'both', 'each', 
			'few', 'more', 'most', 'other', 'some', 'such', 'no', 
			'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 
			'very', 's', 't', 'can', 'will', 'just', 'don', 
			'should', 'now', '']

def clean(line:str) -> str:
    line = line.replace("’", "")
    line = line.replace("'", "") #remove quotes
    line = line.replace("-", " ") #replace hyphens with spaces
    line = line.replace("\t", " ")
    line = line.replace("\n", " ")
    line = line.lower()

    return line


def find_synonyms(word:str) -> List[str]:
    # select list of synonyms for word
    synonyms:List[str] = []
    for syn in wordnet.synsets(word):
        for lm in syn.lemmas():
            synonyms.append(lm.name())

    # filter synonyms to exclude underscored and hyphenated words 
    synonyms = [w for w in synonyms if '_' not in w]
    synonyms = [w for w in synonyms if '-' not in w]

    # remove '' and word from synonyms
    synonyms = [w for w in synonyms if w != '']
    synonyms = [w for w in synonyms if w != word]

    #synonyms_set = set(synonyms)
    #print('subst_synonyms: set of synonyms of ' + word + ' = ' + str(synonyms_set))
    return synonyms


def replace(sa:List[str], maxsubs:int) -> Tuple[List[str], List[List[str]]]:
    print(f'subst_synonyms.replace(): maxsubs = {maxsubs}')

    sa_:List[str] = ["" for i in range(len(sa))]
    words_:List[List[str]] = [[] for i in range(len(sa))] 
    for i in range(len(sa)):
        # initialize sa_[i] and words_[i]
        s = sa[i]
        sa_[i] = s
        words_[i] = []

        #diagnostics
        print(f'\n\nsubst_synonyms.replace [initial]: sa_ = {sa_}')
        print(f'subst_synonyms.replace: words_ = {words_}')

        # clean the sentence of useless punctuation
        s_ = clean(s)
    
        # derive list of words from string sentence s
        sw = re.split(r'[;,\s]\s*', s_) 
        #print('\nsubst_synonyms: sw = ' + str(sw))
    
        # filter words in sentence to exclude stop-words
        sw = [w for w in sw if w not in stop_words]
        print('\n\nsubst_synonyms: filtered sw = ' + str(sw))

        if len(sw) > 0:
            k = 0
            for word in sw:
                print('\n\nsubst_synonyms: candidate replaced WORD = ' + word)
    
                synonyms = find_synonyms(word)

                #diagnostics
                print('\nsubst_synonyms[A]: synonyms of ' + word + ' = ' + str(synonyms))
                print(f'subst_synonyms.replace [A]: sa_ = {sa_}')
                print(f'subst_synonyms.replace: words_ = {words_}')
                print(f'subst_synonyms.replace: len(synonyms) = {len(synonyms)}')


                if len(synonyms) > 0:
                    #w = synonyms_set.pop()  #selects random element from set
                    w = synonyms[0]
                    print(f'\n****** subst_synonyms B[{i}]: synonym of ' + word + ' is ' + w)
                    sa_[i] = sa_[i].replace(word, w)
                    sa_[i] = sa_[i].replace(word.capitalize(), w.capitalize())
                    words_[i].append(word)

                    #diagnostics
                    print(f'subst_synonyms[B{i}]: sa_[{i}] = {sa_[i]}')
                    print(f'subst_synonyms.replace: words_[{i}] = {words_[i]}')


                    k += 1
                    if k >= maxsubs: 
                        break

    return sa_, words_



if __name__ == "__main__": 
    print("subst_synonyms module running in diagnostics mode as __main__")
    sa:List[str] = ['the car - as far as I know - is big', 'He talks to birds']
    maxsubs:int = 3
    sa_, words_ = replace(sa, maxsubs)

    print('\n')
    for i in range(len(sa)):
        print('\nwords_[' + str(i) + '] = ' + str(words_[i]))
        print('original sentence sa[' + str(i) + '] = ' + sa[i])
        print('substitute sentence sa_[' + str(i) + '] = ' + sa_[i])

else:
    print("subst_synonyms module imported")
