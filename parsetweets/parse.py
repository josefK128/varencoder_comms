# parse.py - parsetweets/csv_db/tweetsK -> db/tweetsK

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
dbpath = 'csv_db/' + thread
tweetspath = '../db/' + thread


#create directory at dbpath if needed
if not os.path.exists(dbpath):
    mode = 0o777
    os.mkdir(dbpath, mode)
    #open(pdfgenpath, 'w').close()
    print(f'created directory {dbpath}')


# parse files in thread
# filepath is path in parsetweets/csv_db; filepath_ is path in ../db
for filename in os.listdir(dbpath):
    if filename.endswith('.csv'):
        filepath = os.path.join(dbpath, filename)
        print('---------------------------------------------------')
        print('filepath = ' + filepath)
    
        # parse email file
        with open(filepath) as f:
            fcsv = csv.DictReader(f)
            i = 0
            for row in fcsv:
                data:Dict = {}
                msg:str
                print('i = ' + str(i) + '  row = ' + str(row))
                msg = row['tweet']
                filename_ = filename.replace('.csv', str(i) + '.json')
                i += 1
                filepath_ = os.path.join(tweetspath, filename_)
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

