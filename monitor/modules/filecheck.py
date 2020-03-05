import os, sys, pwd



######################
# need path for logs, config
#
#
def root_warning():
    return print('SCRIPT SHOULD NOT BE RUN AS ROOT!')

def check_files():
    """ If base directory isn't present it is created also checks individually for logs 
    and config dir and creates if needed
    """    
    # debug_logger = logger.get_logger()
    # debug_logger.debug('Checking for needed directories')
    # try block added to check if script is running as root
    # throws an error if it is unless running in a container (set by ENV variable in Dockerfile) which is build environment
    try:
        base_path = f'/home/{pwd.getpwuid(os.getuid())[0]}/monitor/'
    except OSError as e:
        if os.getuid() == 0 and os.environ['CONTAINER']:
            pass
        else:
            root_warning()
            sys.exit(1)
    try:        
        os.makedirs(os.path.join(base_path, 'logs'))
    except OSError:
        root_warning()
        sys.exit(1)
    else:
        # debug_logger.debug('Base Path not found, creating logs and config directories')
        # create log directory
        try:
            os.makedirs(os.path.join(base_path, 'logs'))
            # create settings directory
        except OSError:
            root_warning()
        except FileExistsError:
            pass
        try:
            
            os.makedirs(os.path.join(base_path, 'config'))
    elif not os.path.exists(os.path.join(base_path, 'logs')):
        os.makedirs(os.path.join(base_path, 'logs'))
    elif not os.path.exists(os.path.join(base_path, 'config')):
        os.makedirs(os.path.join(base_path, 'config'))


check_files()
