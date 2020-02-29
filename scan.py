import os, sys
import subprocess
import json
import modules.logs as logger
import modules.suppress as sp
import time as t
import modules.filecheck

critical_logger = logger.get_logger(50, 'critical')
debug_logger = logger.get_logger()
info_logger = logger.get_logger(30, 'info')

def load_config():
    """ Loads json config file and returns
    """ 
    try:
        with open('config/monitor.json', 'r') as f:
            config = json.load(f)
    
    except IOError:
        debug_logger.critical('config file missing, creating default')
        config = {'settings' : {'interval' : '60', 'servers' : ['localhost',]}}
    else:
        debug_logger.debug('Config File Loaded')
        config = json.dumps(config)
        config = json.loads(config)
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
    # config = json.dumps(config)

    while True:
        for s in config['settings']['servers']:
        
            with sp.suppress_stdout():
                response = subprocess.call(['ping',f'{s}','-c','1',"-W","3"], False)
                if response == 0:
                    info_logger.info(f'{s} is up...')
                elif response == 1:
                    info_logger.info(f'{s} is down...')
                else:
                    critical_logger(f'Unknown Error occured trying to reach {s}')
            interval = int(config['settings']['interval'])
            t.sleep(interval)



if __name__ == "__main__":
    main()