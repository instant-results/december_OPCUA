import sys
from opcua import Server
from random import randint
import time

server = Server()

url = "opc.tcp://127.0.0.1:9001"
server.set_endpoint(url)

name = "OPCUA_SERVER"
addspace = server.register_namespace(name)

# Get the Objects node
objects = server.get_objects_node()

# Populate the namespace
myobj = objects.add_object(addspace, "MyObject")
myvar = myobj.add_variable(addspace, "MyVariable", 6.7)
myvar2 = myobj.add_variable(addspace, "MyVariable2", 123)
#myvar is now writable on the client side
myvar.set_writable()

# Start the server
server.start()

# Run the server forever
try:
    while True:
        
        myvar.set_value(randint(0, 20))
        myvar2.set_value(randint(0, 20))
        print(f"myvar = {myvar.get_value()}   myvar2 = {myvar2.get_value()}" )

        time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    # Close the server
    print("Server stop")
    server.stop()
    sys.exit()