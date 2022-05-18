import configparser as cp

VARIABLE_SECTION = 'OBD_VARIABLES'
DB_SECTION = 'DATABASE'

VARIABLES_AND_TIME = {}


def get_config():
    config = cp.ConfigParser()
    config.read('config.ini')
    for var in config[VARIABLE_SECTION]:
        VARIABLES_AND_TIME[var.upper()] = config[VARIABLE_SECTION][var]
    # print(VARIABLES_AND_TIME)
    return VARIABLES_AND_TIME


def get_db_name():
    config = cp.ConfigParser()
    config.read('config.ini')
    return config[DB_SECTION]['raw_db_name']

def get_clean_db_name():
    config = cp.ConfigParser()
    config.read('config.ini')
    return config[DB_SECTION]['clean_db_name']