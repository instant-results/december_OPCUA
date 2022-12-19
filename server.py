import sys
from opcua import Server

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

# Start the server
server.start()

# Run the server forever
try:
    while True:
        pass
except (KeyboardInterrupt, SystemExit):
    # Close the server
    server.stop()
    sys.exit()