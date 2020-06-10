# msg2sentences.py
# -*- coding: utf-8 -*-
import re
from typing import List



# vars for text.replace and re.sub in function split_into_sentences
alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"


# split_into_sentences
def split_into_sentences(text:str) -> List[str]:
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
#    text = text.replace(".",".<stop>")
    text = text.replace(". ",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")

    residue = text

    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]

    if sentences == []:
        sentences = residue[0:4]

    return sentences




if __name__ == "__main__": 
    print('\n\n+++++++++++ msg2sentences +++++++++++++++++++++')
    print("msg2sentences module running as __main__")
    text = """
The Security Interest Group is a forum for vendors and developers to discuss\nthe state of standardization and development agendas for security technologies\nacross all the various venues for standardization.\n\nThe inaugural meeting is May 24th, to be held simultaneously 8AM-4PM PST at\nOracle in Redwood Shores, and 11AM-7PM at MIT/LCS with audio- and\nweb-conferencing.\n\nThis mailing list is public, though not publicized. Anyone may subscribe, and\na web-based archive is at http://www.w3.org/pub/WWW/Archives/Public/sig/ .\nSend the command \"subscribe [email]\" or \"unsubscribe [email]\" in the Subject\nline or body of a message to sig-request@w3.org.\n\nThanks,\nRohit Khare\n\n---\nRohit Khare -- 617/253-5884\nTechnical Staff, World Wide Web Consortium\nNE43-354, MIT LCS, Cambridge, MA 02139
    """
    sentences = split_into_sentences(text)

    # diagnostics
    print('\n')
    index = 0
    for s in sentences:
        print('sentence['+str(index)+'] = ' + s)
        index += 1

else:
    print("msg2sentences module imported")
