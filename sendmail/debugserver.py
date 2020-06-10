# DebuggingServer

import smtpd
import asyncore
from typing import Tuple


host = '127.0.0.1'  #localhost
port = 1025
remoteaddr:Tuple[str,int] 

server = smtpd.DebuggingServer((host, port), None)
#server = smtpd.DebuggingServer((host, port), remoteaddr)

asyncore.loop()
