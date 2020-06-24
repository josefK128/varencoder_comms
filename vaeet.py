# vaeet.py 
#
# vaee => Variational AutoEncoder (for emails - variable number of synonym 
# substitutions per sentence given by cmdline argv[2] 'maxsubs' default=3)
#
# For emails, further semantic generative transformation is done in @vae
# which first transforms the json-containers for thread(s) of emails into
# the @vae document format read by the encoder of @vae.
# The encoder is a Variational Encoder using encoding produced by
# a Singular Value Decomposition (SVD) of the document-term matrix A
# SVD: A(nxm) = U(nxk) * S(kxk) * Vt(kxm) 
# variations are translations to close vectors in the semantic feature space U
# decoder is the mapping from the semantic feature space point (row-vector of U)
# to its corresponding sentence associated with the same row-vector in the 
# document-term matrix A


import os.path
from os import path
import time
import nltk
import sys
import json
sys.path.insert(0, './src')
import msg2sentences as msg2s 
import subst_synonyms as synonyms


#nltk.download()


# determine maxsubs
if len(sys.argv) > 2:
    maxsubs:int = int(sys.argv[2])
    thread:str = sys.argv[1]
else:
    maxsubs = 3

    # determine thread
    if len(sys.argv) > 1:
        thread = sys.argv[1]
    else:
        thread = 'thread0'

print('\nmaxsubs = ' + str(maxsubs))
print('thread = ' + thread)



# vars
directory = './db/' + thread
directory_ = './db_/' + thread



def action(diagnostics:bool=False) -> None:
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            filepath_ = os.path.join(directory_, filename)
            print('---------------------------------------------------')
            print('filepath = ' + filepath)
            print('filepath_ = ' + filepath_)
    
            # parse email file
            with open(filepath, 'r') as f:
                data = json.load(f)
                msg = data['msg']
                msg_ = ''
                data_ = {}
    
    
                # separate sentences from msg of data object
                sentences = msg2s.split_into_sentences(msg)
                if diagnostics:
                    print('\nvaee: no. of sentences in msg = ' + str(len(sentences)))
                    print('\nvaee: sentences in msg = ' + str(sentences))
    
    
                # substitute synonyms for word in each sentence and return both
                sentences_, words_ = synonyms.replace(sentences, maxsubs)
                if diagnostics:
                    print('\n\nvaee: *** after synonym substitution sentences are:')
                    for index in range(len(sentences)):
                        print('\nwords_['+str(index)+'] = ' + str(words_[index]))
                        print('sentence['+str(index)+'] = ' + sentences[index])
                        print('sentence_['+str(index)+'] = ' + sentences_[index])
    
    
                # prepare json-container data_ for new email with the same content 
                # as the ingested json-container data, but altered msg
                data_['sender'] = data['sender'] or ''
                data_['receivers'] = data['receivers'] or [] 
                data_['sent'] = data['sent'] or ''
                data_['subject'] = data['subject'] or '' 
                msg_ = msg_.join(sentences_)
                data_['msg'] = msg_ 
                if diagnostics:
                    print("\nvaee: data_['msg'] = " + data_['msg'])
    
    
                # write data_ as json to db_ at filepath_ 
                data_json = json.dumps(data_, indent = 4, sort_keys=True)
                with open(filepath_, 'w+') as f:
                    f.write(data_json)
                    f.write('\n')
                    f.close()
                    if diagnostics:
                        print("\nvaee: wrote data_json to " + filepath_)

 


if __name__ == "__main__": 
    print('\n\n+++++++++++ vaee +++++++++++++++++++++')
    print("vaee module running as __main__")
    action(True)
else:
    print("vaee module imported")
