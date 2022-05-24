import configparser as cp

VARIABLE_SECTION = 'OBD_VARIABLES'
DB_SECTION = 'DATABASE'
FORCE_SECTION = 'FORCE_VARIABLES'

VARIABLES_AND_TIME = {}
FORCE_VARIABLES = []


def get_config():
    config = cp.ConfigParser()
    config.read('config.ini')
    for var in config[VARIABLE_SECTION]:
        VARIABLES_AND_TIME[var.upper()] = config[VARIABLE_SECTION][var]
    # print(VARIABLES_AND_TIME)
    return VARIABLES_AND_TIME


def get_force_variables():
    config = cp.ConfigParser()
    config.read('config.ini')
    for var in config[FORCE_SECTION]:
        FORCE_VARIABLES.append(var)
    return FORCE_VARIABLES

def get_db_name():
    config = cp.ConfigParser()
    config.read('config.ini')
    return config[DB_SECTION]['raw_db_name']

def get_clean_db_name():
    config = cp.ConfigParser()
    config.read('config.ini')
    return config[DB_SECTION]['clean_db_name']