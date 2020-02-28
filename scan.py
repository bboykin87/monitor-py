import os, sys
import subprocess
import configparser
import json

def main():
    if not os.path.exists("/etc/monitor/monitor.conf"): 
        os.makedirs("/etc/monitor/")
        config['settngs'] = {'interval' : '60', 'servers' : ['localhost',]}
        config_json = json.dumps(config)
    with open('monitor.json') as f:
        data = json.load(f)
        

    

while
r =subprocess.call(["ping", "192.168.1.241", "-c", "1"])
