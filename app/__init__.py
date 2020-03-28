from flask import Flask
import os
import json

flask_app=Flask(__name__)


if not os.path.exists("app/ip.json"):
    ip = open("app/ip.json","w")
    currentIP  = {}
    currentIP['ipaddr'] = "-1"

    json.dump(currentIP,ip)
    ip.close()


from app import routes,config