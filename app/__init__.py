from flask import Flask
import os
from json import dump,load

flask_app=Flask(__name__)
flask_app.config.TEMPLATES_AUTO_RELOAD = True
flask_app.secret_key = 'aS1sIY4VK4Dy0S5iNTIRVKc-tEYsKrNIQs6lPHLdadI'

current_path = os.path.abspath(__path__[0])
config_file_folder = 'config Files'

config_file_path = os.path.join(current_path,config_file_folder,'config.json')
ip_file_path = os.path.join(current_path,config_file_folder,'ip.json')


if not os.path.exists(ip_file_path):
    ip = open(ip_file_path,"w")
    currentIP  = {}
    currentIP['ipaddr'] = "-1"

    dump(currentIP,ip)
    ip.close()

if not os.path.exists(config_file_path):
    configFile = open(config_file_path,"w")
    configInfo  = {}
    configInfo['configured'] = 0
    configInfo['drive'] = ""
    configInfo['dfolder'] = "1 Shared files1"
    dump(configInfo,configFile)
    configFile.close()


from app import routes,config