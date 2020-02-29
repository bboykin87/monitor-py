import os, sys
import subprocess
import json
import modules.logs as logger
import modules.suppress as s
import time as t
critical_logger = logger.get_logger(50, 'critical')
debug_logger = logger.get_logger()
info_logger = logger.get_logger(30, 'info')

def load_config():
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
    return config

def ping_server(host):
    """ Pings all servers in the passed list and logs if they are up or down
    
    Arguments:
        host {list} -- [list of hosts to ping]
    """    
    for s in host:
        with s.suppress_stdout():
            response = subprocess.call(['ping',f'{host}','-c','1',"-W","3"], False)
            if response == 0:
                info_logger.info(f'{s} is up...')
            elif response == 1:
                info_logger.info(f'{s} is down...')

def main():
    config = load_config()
    # config = {
        # 'settngs' : [{'interval' : '60', 'servers' : ['localhost',]}]
        # }
    config = json.dumps(config)

    while True:
        for s in config['settings']['servers']:
        
            with s.suppress_stdout():
                response = subprocess.call(['ping','192.168.1.141','-c','1',"-W","3"], False)
                if response == 0:
                    info_logger.info(f'{s} is up...')
                elif response == 1:
                    info_logger.info(f'{s} is down...')
    interval = int(config['settings']['interval'])
    t.sleep(f'{interval}')



if __name__ == "__main__":
    main()