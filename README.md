__VAE_et README.md__

This module synthesizes tweets and singular emails - that is, emails which do not belong to a corpus of similar emails, either by author or subject. Tweets by nature are always considered singular.



Setup:


* install python 3.X (current latest 3.8.X) - see 
  https://www.python.org/downloads/ - simply click download button and follow defaults for installation
  
  
  
* clone the repo

* The main synthesis software is vaeet.py which creates variations on emails and tweets in /db by substitution of synonyms. Resulting email and/or tweet variations are written to /db_.  Secondary python modules are in /src. 
  Supplementary applications to prepare emails and tweets for variation are in /parsemail and /parsetweets. These directories contain json-emails and csv-tweets and modules parse.py which write them to /db as text-files as expected by vaeet.py.

  

* install dependencies - either in virtual environment  (see documentation python module venv) or else globally:

  root> pip install -r requirements.txt   

  ​                             

* application usage:  
  
  * parsemail> py parse.py <collection-name> - reads w3c-emails_db/<collection-name>/*.txt
    (text-files containing email information (possibly empty) name:<name>, email:<email-address>, sent:<date>, subject:<subject> and the body consisting of the email message.)  

    
    
   * parsetweets> py parse.py <collection-name> - reads <collection-name>/file.csv
      (csv-file containing one or more tweets under column one labeled 'tweets'
      and consisting of rows of tweets from 2 to N.
  
      
      
  * vaeet> py vaeet.py <collection-name-in-db>  [maximum-synonym
    substitutions-per-sentence - default 5 per sentence]
    (reads all email-json-files in db/<collection-name-in-db> substitutes
    synonyms for the prescribed number of substitutions per sentence and write
    a new email-json-file to /db_.)
    
    


* Exp of email-json-file format: 
{
    "msg": "\n     \n   \nThe Security Interest Group is a forum for vendors and developers to discuss\nthe state of standardization and development agendas for security technologies\nacross all the various venues for standardization.\n\nThe inaugural meeting is May 24th, to be held simultaneously 8AM-4PM PST at\nOracle in Redwood Shores, and 11AM-7PM at MIT/LCS with audio- and\nweb-conferencing.\n\nThis mailing list is public, though not publicized. Anyone may subscribe, and\na web-based archive is at http://www.w3.org/pub/WWW/Archives/Public/sig/ .\nSend the command \"subscribe [email]\" or \"unsubscribe [email]\" in the Subject\nline or body of a message to sig-request@w3.org.\n\nThanks,\nRohit Khare\n\n---\nRohit Khare -- 617/253-5884\nTechnical Staff, World Wide Web Consortium\nNE43-354, MIT LCS, Cambridge, MA 02139\n\n\n",
    "receivers": [
        " sig@w3.org\n",
        " hal@mit.edu",
        " timbl@w3.org\n"
    ],
    "sender": "\"khare@pest.w3.org\"\n",
    "sent": "\"Fri, 17 May 96 17:13:00 -0400\"\n",
    "subject": "\"Welcome to the Security Interest Group mailing list\"\n"
}



* Example command line uses: 
  * src/parsemail> py parse.py  phishing1  
  * src/parsetweets> py parse.py  tweets1
  * root> py vaeet.py  phishing1  7  (non-default maximum synonym substitutions per sentence - 7)
  
