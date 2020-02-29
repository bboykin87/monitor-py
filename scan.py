import os, sys
import subprocess
import json
import modules.logs as logger




def main():
    
    config = {
        'settngs' : [{'interval' : '60', 'servers' : ['localhost',]}]
        }
    config_json = json.dumps(config)

    with open('monitor.json') as f:
        json.dump(config_json, f)


        

    

while
r =subprocess.call(["ping", "192.168.1.241", "-c", "1"])
