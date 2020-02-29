import os, sys
import subprocess
import json
import modules.logs as logger

critical_logger = logger.get_logger(50, 'critical')
debug_logger = logger.get_logger()

def get_config():
""" Loads json config file and returns
""" 
    try:
        config = json.load('config/monitor.json')
    except AttributeError:
        debug_logger.critical('config file missing, creating default')
        config = {
            'settngs' : [{'interval' : '60', 'servers' : ['localhost',]}]
            }
    else:
        debug_logger.debug('Config File Loaded')

def main():
    
    config = {
        'settngs' : [{'interval' : '60', 'servers' : ['localhost',]}]
        }
    config_json = json.dumps(config)

    with open('monitor.json') as f:
        json.dump(config_json, f)


        

    

while
r =subprocess.call(["ping", "192.168.1.241", "-c", "1"])
