###############
import socket
import sys
from time import *
from datetime import datetime
#################
On_IBlack="\[\033[0;100m\]"
On_IRed="\[\033[0;101m\]"
IRed="\[\033[0;91m\]"
BRed="\[\033[1;31m\]"
BBlue="\[\033[1;34m\]"
Red="\[\033[0;31m\]"
################
print('\033[0;91m\ _____       _   _   _   ')
print('/  ___/     | | | | / /  ')
print('| |___      | | | |/ /   ')
print('\___  \  _  | | | |\ \   ')
print(' ___| | | |_| | | | \ \  ')
print('/_____/ \_____/ |_|  \_')
print('\033[1;34m make with sajad.JK')




ip=input ("\===> ENTER YOUR IP TO START: ")
t1=datetime.now()
print("Scanning Start.. %s Please Wait.. "%ip)
sleep(1)
####################
try:
    for port in range(1,6553):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        if(s.connect_ex((ip,port))==0):
            try:
                serv=socket.getservbyport(port)

            except socket.error:
                serv="Unknown Service"
            print ("Port %s Open Service:%s "%(port,serv))
        t2=datetime.now()
        t3=t2-t1
    print ("\033[0;31m\Scanning Completed On %s"%t3)
except KeyboardInterrupt:
    print("\033[0;31m\See You Soon....!")
###############################

