# ## pip list | findstr /I obd
# ## Downgrade obd to v0.6.1
# ## Trocar async pra asyncn (arquivo e imports na lib python - C:\Users\UbivisNb05\AppData\Local\Programs\Python\Python37\Lib\site-packages\obd)
#
# ## LINK PARA COMANDOS OBD - https://python-obd.readthedocs.io/en/latest/Command%20Tables/
import obd
import sched, time
import configuration
from database import Database
db = Database()

# Ativa DEBUGGER do OBD
obd.logger.setLevel(obd.logging.DEBUG)

# Conecta ao adaptador OBD-II
ports = obd.scan_serial()
print("Portas: ")
print(ports)

connection = obd.OBD(portstr=ports[0])

# Print supported commands
commands = connection.supported_commands
print("Supported commands: ")
for command in commands:
    print(command.name)

starttime = time.time()
s = sched.scheduler(time.time, time.sleep)


def collect_variable(sc,variable_name, variable_time):
    print("COLLECT = ", variable_name, variable_time)
    try:
        response = connection.query(obd.commands[command])
        db.insert_values(variable_name, response.value)
        print('DADO = ', variable_name, response.value)
    except Exception as ex:
        print("Error: " + str(ex))
    sc.enter(int(variable_time), 1, collect_variable, (sc,variable_name,variable_time))


for obd_variable_name, obd_variable_time in configuration.get_config().items():
    print('SCHEDULED = ', obd_variable_name, obd_variable_time)
    s.enter(int(obd_variable_time), 1, collect_variable, (s,obd_variable_name, obd_variable_time))
s.run()


# Send a command
# while True:
#     if keyboard.is_pressed('q'):
#         break
#     print(int(60.0 - ((time.time() - starttime) % 60.0)))
    # try:
    #     response = connection.query(obd.commands[command])
    #     print(response.value)
    # except Exception as ex:
    #     print("Error: " + str(ex))

# Close the connection
# connection.close()
#
# #####################################################
#

# # cmd = obd.commands.FUEL_LEVEL
# # response = connection.query(cmd)
# # print(reponse.value)
#
# # cmd = obd.commands.RPM
# # response = connection.query(cmd)
# # print(reponse.value)
#
# # cmd = obd.commands.SPEED
# # response = connection.query(cmd)
# # print(reponse.value)


###########################
# USANDO O BANCO DE DADOS #
###########################


# from database import Database
# import random
#
# db = Database()
#
# while True:
#     db.insert_values(key, value)