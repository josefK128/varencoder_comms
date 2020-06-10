# parse.py - tweets

import os
import sys
import re
import json
import csv
from typing import List, Dict


# determine thread
if len(sys.argv) > 1:
    thread = sys.argv[1]
else:
    thread = 'tweets1'
print('thread = ' + thread)


# vars
directory = 'csv_db/' + thread
directory_ = '../db/' + thread


# parse files in thread
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        filepath = os.path.join(directory, filename)
        print('---------------------------------------------------')
        print('filepath = ' + filepath)
    
        # parse email file
        with open(filepath) as f:
            fcsv = csv.DictReader(f)
            i = 0
            #fname = os.path.basename(f.name)
            #print(f'\n\n\nfilename = {fname}')
            for row in fcsv:
                print(f'\n\n\nparse1: row[{i}] = {row}')
                data:Dict = {}
                msg:str
                #print('row = ' + str(row))
                msg = row['tweet']

                #msg = msg.replace('@', '\@')

                print(f'\nparse2: msg = {msg}')
                    

                filename_ = filename.replace('.csv', str(i) + '.json')
                i += 1
                filepath_ = os.path.join(directory_, filename_)
                data['msg'] = msg
                data['sender'] = ''
                data['receivers'] = []
                data['sent'] = ''
                data['subject'] = ''
                data_json = json.dumps(data, indent = 4, sort_keys=True)
                print('\ndata_json = ')
                #[print(key, value) for key, value in data.items()]
                print(data_json)

                # write data as json to db_
                with open(filepath_, 'w+') as f:
                    f.write(data_json)
                    f.close()

