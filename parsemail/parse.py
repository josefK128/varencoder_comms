# parse.py - emails

import os
import sys
import re
import json
from typing import List, Dict


# determine thread
if len(sys.argv) > 1:
    thread = sys.argv[1]
else:
    thread = 'thread0'
print('thread = ' + thread)


# vars
data:Dict = {}
receivers:List[str] = []
msg = ""
mail_regex = '^[A-Za-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
emailpath = 'w3c-emails_db/' + thread
dbpath = '../db/' + thread


#create directory at dbpath if needed
if not os.path.exists(dbpath):
    mode = 0o777
    os.mkdir(dbpath, mode)
    #open(pdfgenpath, 'w').close()
    print(f'created directory {dbpath}')


# parse files in thread - filepath is path in email/  filepath_ is path in db/
for filename in os.listdir(emailpath):
    filepath = os.path.join(emailpath, filename)
    filename_ = filename.replace('.txt', '.json')
    filepath_ = os.path.join(dbpath, filename_)
    print('---------------------------------------------------')
    print('filepath = ' + filepath)
    print('filepath_ = ' + filepath_)

    # parse email file
    with open(filepath, 'r') as f:
        for line in f:
            if line.startswith('email='):
                data['sender'] = line[6:]
                continue
            if line.startswith('subject='):
                data['subject'] = line[8:]
                continue
            if line.startswith('To:'):
                receivers = [line[3:]]
                continue
            if line.startswith('Cc:'):
                a = line[3:].split(',')
                for e in a:
                    receivers.append(e)
                continue
            if line.startswith('docno='):
                continue
            if line.startswith('name='):
                continue
            if line.startswith('sent='):
                data['sent'] = line[5:]
                continue
            if line.startswith('Initial subscriber list:'):
                break
            if re.search(mail_regex, line):
                continue
            #if line == "\n":
            #    continue
            msg += line

        # print data result for email file as json
        data['receivers'] = receivers
        data['msg'] = msg
        data_json = json.dumps(data, indent = 4, sort_keys=True)
        print('\ndata = ')
        #[print(key, value) for key, value in data.items()]
        print(data_json)


        # write data as json to db_
        with open(filepath_, 'w+') as f:
            f.write(data_json)
            f.close()

