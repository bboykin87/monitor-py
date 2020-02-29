import os, sys
import subprocess
import json
import modules.logs as logger
# import modules.suppress as sp
import time as t
import modules.filecheck

_logger = logger.get_logger(__name__)


def load_config():
    """ Loads json config file and returns
    """ 
    try:
        with open('config/monitor.json', 'r') as f:
            config = json.load(f)
    
    except IOError:
        _logger.debug('config file missing, creating default')
        config = {'settings' : {'interval' : '60', 'servers' : ['localhost',]}}
    else:
        _logger.debug('Config File Loaded')
        config = json.dumps(config)
        config = json.loads(config)
    return config


def ping_server(host):
    """ Pings all servers in the passed list and logs if they are up or down
    
    Arguments:
        host {list} -- [list of hosts to ping]
    """    
        # with s.suppress_stdout():
    response = subprocess.call(['ping',f'{host}','-c','1',"-W","3"], False)
    return response

def main():
    config = load_config()
    # config = {
        # 'settngs' : [{'interval' : '60', 'servers' : ['localhost',]}]
        # }
    # config = json.dumps(config)

    while True:
        for s in config['settings']['servers']:
            response = ping_server(s)
        if response == 0:
            _logger.info(f'{s} is up...')
        elif response == 1:
            _logger.info(f'{s} is down...')
        interval = int(config['settings']['interval'])
        t.sleep(interval)



if __name__ == "__main__":
    main()