## pip list | findstr /I obd
## Downgrade obd to v0.6.1
## Trocar async pra asyncn (arquivo e imports na lib python - C:\Users\UbivisNb05\AppData\Local\Programs\Python\Python37\Lib\site-packages\obd)

## LINK PARA COMANDOS OBD - https://python-obd.readthedocs.io/en/latest/Command%20Tables/
import obd

# Ativa DEBUGGER do OBD
obd.logger.setLevel(obd.logging.DEBUG)

# Conecta ao adaptador OBD-II
ports = obd.scan_serial()
print("Portas: ")
print(ports)

connection = obd.OBD()

# Print supported commands
commands = connection.supported_commands
print("Supported commands: ")
for command in commands:
  print(command.name)

# Send a command
while True:
  command = input("Enter command (type 'quit' to exit): ")
  if (command == "quit"):
    break
  try:
    response = connection.query(obd.commands[command])
    print(response.value)
  except Exception as ex:
    print("Error: " + str(ex))

# Close the connection
connection.close()

#####################################################

#cmd = obd.commands.FUEL_LEVEL
#response = connection.query(cmd)
#print(reponse.value)

#cmd = obd.commands.RPM
#response = connection.query(cmd)
#print(reponse.value)

#cmd = obd.commands.SPEED
#response = connection.query(cmd)
#print(reponse.value)