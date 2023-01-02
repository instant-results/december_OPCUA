from opcua import Client

client = Client("opc.tcp://127.0.0.1:9001")
try: 
    client.connect()
except:
    print("Couldn't connect to the server")
else: 
    myvar = client.get_node("ns=2;i=2")
    print("test")

    root = client.get_root_node()
    print("Root node is: ", root)

    objects = client.get_objects_node()
    print("Objects node is: ", root)

    myvar = root.get_child(["0:Objects", "2:MyObject", "2:MyVariable"])
    obj_root = root.get_child(["0:Objects", "2:MyObject"])
    print("myvar is: ", myvar)
    print("root is: ", obj_root)

    print("values of root node ", client.get_values([root]))


    client.disconnect()