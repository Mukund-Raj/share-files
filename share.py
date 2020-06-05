#!E:\flask_tutorial\venv\Scripts\python.exe
from app import flask_app,config_file_path,ip_file_path
from app.config import Getdrives
import argparse
import re
import os
import sys
import json

ISDEBUG = 1

localip='127.0.0.1'

IPregex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''

#path for the ip file

def saveIP():
    ip = open(ip_file_path,"w")
    currentIP ={}
    currentIP['ipaddr'] = args.ip
    json.dump(currentIP,ip)
    ip.close()

#return the saved IP address if the user had wished to do so
def getIP():
    ipfile = open(ip_file_path,'r')
    
    currentIP = json.load(ipfile)
    
    if currentIP['ipaddr'] == "-1":
        print("IP doesn't exist, please specify IP via -ip = 'IP address' and save it through -s 1 when running the program")
        sys.exit("NO USER IP PRESENT")

    else:
        return currentIP['ipaddr']
    ipfile.close()

#actual running for the server
def runTheServer():
    print()
    print("GO TO ",thisPCIP,':',thisPCPORT,' to share files')
    print()
    try:
        flask_app.run(host = thisPCIP,port = thisPCPORT,debug=ISDEBUG)
    except OSError:
        print("\n\n Please connect your PC to a network\n\n")

if __name__ == "__main__":
    
    #ip and port for the server
    thisPCIP=""
    thisPCPORT=9999
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip"\
        ,help="Enter your Computer IP address\n Ex: type ipconfig in cmd and \n look for your Wireless LAN adapter Wi-fi or if you are connected to router via ethernet then look for ethernet adapter and look for IPv4 address in them OR \n Look for readme.txt file in the installation folder of it")
    
    parser.add_argument("-port",help="If you want to change the port number")
    parser.add_argument("-s",help="Do you want to save IP for later use enter 1 for yes",type=int)
    
    args = parser.parse_args()
    #start config file
    configfile = open(config_file_path,'r+')
    drives = Getdrives()
    cfg = json.load(configfile)
    if not cfg['configured']:
        print("DRIVES on your computer")
        for d in drives:
            print("\t",d)

        print()
        dlDrive = input("Where you want to stored files::")
        dlDrive = dlDrive.upper()
        if dlDrive in drives:
            cfg['configured'] = 1
            cfg['drive']=dlDrive
            cfg['dfolder']="1 Shared files1"
            configfile.truncate(0)
            configfile.seek(0)
            json.dump(cfg,configfile)
            print()
            print("You can change the drive settings in config.json file in app")
            print()
    configfile.close()
    #end config file


    #setting the port for the server
    if args.port:
        thisPCPORT = args.port
        
    if args.ip:
        if re.search(IPregex,args.ip) :

            #if ip.json file exists then simply store the IP in that file
            thisPCIP = args.ip
            if args.s:
                if os.path.exists(ip_file_path):
                    saveIP()
                #otherwise create it
                else:
                    open(ip_file_path)
                    saveIP()
            runTheServer()
        else:
            print("invalid ip,please enter a valid IP")

    else:
        if os.path.exists(ip_file_path):
            #print("yes file  exists")
            thisPCIP = getIP()
            runTheServer()
        else:
            with open(ip_file_path) as ipfile:
                currentIP  = {}
                currentIP['ipaddr'] = "-1"
                json.dump(currentIP,ipfile)

            print("IP doesn't exist please specify IP via -ip = 'IP address'\n for help enter share.py --help or -h")
            sys.exit("NO USER IP PRESENT")
    
