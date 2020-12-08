from pymodbus.client.sync import ModbusTcpClient


host = ""
port = 0
host = input("host IP: ")
port = int(input("host port: "))
client = ModbusTcpClient(host, port)
while True:
    print("1. Read Register")
    print("2. Read Coil")
    print("3. Write Register")
    print("4. Write Coil")
    print("q. To Quit")
    operation = input("operation: ")
    if operation == "1":
        address = int(input("adress: "))
        value = int(input("many: "))
        try:
            client.connect()
            req=client.read_holding_registers(address,value)
            print(req.registers)
            client.close()
        except Exception as e:
            print(e)
    if operation == "2":
        address = int(input("adress: "))
        value = int(input("many: "))
        try:
            client.connect()
            req=client.read_coils(address,value)
            print(req.bits)
            client.close()
        except Exception as e:
            print(e)
    if operation == "3":
        address = int(input("adress: "))
        value = int(input("value: "))
        try:
            client.connect()
            req=client.write_register(address,value)
            print(req)
            client.close()
        except Exception as e:
            print(e)
    if operation == "4":
        address = int(input("adress: "))
        value = int(input("value: "))
        try:
            client.connect()
            req=client.write_coil(address,value)
            print(req)
            client.close()
        except Exception as e:
            print(e)
    if operation == "q":
        break
    print("----------")
    print("")