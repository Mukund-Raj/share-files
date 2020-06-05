from app import flask_app,config_file_path,ip_file_path
from app.config import drives
import argparse
import re
import os
import sys
import json

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