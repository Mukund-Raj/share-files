from flask import Flask
import os
import json

flask_app=Flask(__name__)

current_path = os.path.abspath(__path__[0])
config_file_folder = 'config Files'

config_file_path = os.path.join(current_path,config_file_folder,'config.json')
ip_file_path = os.path.join(current_path,config_file_folder,'ip.json')


if not os.path.exists(ip_file_path):
    ip = open(ip_file_path,"w")
    currentIP  = {}
    currentIP['ipaddr'] = "-1"

    json.dump(currentIP,ip)
    ip.close()

if not os.path.exists(config_file_path):
    configFile = open(config_file_path,"w")
    configInfo  = {}
    configInfo['configured'] = 0
    configInfo['drive'] = ""
    configInfo['dfolder'] = "1 Shared files1"
    json.dump(configInfo,configFile)
    configFile.close()


from app import routes,config