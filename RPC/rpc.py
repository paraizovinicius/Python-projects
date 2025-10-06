# Needed imports
import json
import socket
import inspect
from threading import Thread

SIZE=1024

class RPCClient:
    def __init__(self, host:str='localhost', port:int=8080) -> None:
        self.__sock = None
        self.__address = (host, port)

    def connect(self):
        try:
            self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__sock.connect(self.__address)
        except EOFError as e:
            print(e)
            raise Exception('Client was not able to connect.')
    
    def disconnect(self):
        try:
            self.__sock.close()
        except:
            pass


    def __getattr__(self, __name: str):
        def excecute(*args, **kwargs):
            self.__sock.sendall(json.dumps((__name, args, kwargs)).encode())

            response = json.loads(self.__sock.recv(SIZE).decode())
   
            return response
        
        return excecute


class RPCServer: # Irá rodar em 0.0.0.0:8080 por default
    #Constructor
    def __init__(self, host:str='0.0.0.0', port:int=8080) -> None: # port=8080: default TCP port where clients connect.
        self.host = host
        self.port = port
        self.address = (host, port) 
        self._methods = {} # dictionary where function names are stored

    # Here, you pass a function and then it stores it in the dictionary (_methods) with its name as key.
    def registerMethod(self, function) -> None:
        try:
            self._methods.update({function.__name__ : function})
        except:
            raise Exception('A non function object has been passed into RPCServer.registerMethod(self, function)')
        
    # def registerInstance(self, instance=None) -> None:
    #     try:
    #         # Regestring the instance's methods
    #         for functionName, function in inspect.getmembers(instance, predicate=inspect.ismethod):
    #             if not functionName.startswith('__'):
    #                 self._methods.update({functionName: function})
    #     except:
    #         raise Exception('A non class object has been passed into RPCServer.registerInstance(self, instance)')
    
    # handle each client request
    # To do so, private method __handle__
    # params: socket and a tuple representing the client’s address.
    def __handle__(self, client:socket.socket, address:tuple) -> None:
        print(f'Managing requests from {address}.')
        # while loop to manage each receiving request
        while True:
            try:                                # client.recv(SIZE): waits for data from client (in bytes).
                                                # .decode() the message into a readable string format
                                                # JSON.loads() --> transform to object
                # ["function_name", [args...], {kwargs...}]
                functionName, args, kwargs = json.loads(client.recv(SIZE).decode())
                # Everything over the socket is just bytes. 
                # Here, JSON is used to encode/decode data so both sides understand it.
                
            except: 
                print(f'! Client {address} disconnected.')
                break
            # Showing request Type
            print(f'> {address} : {functionName}({args})')

            try:
                response = self._methods[functionName](*args, **kwargs)
            except Exception as e:
                # Send back exeption if function called by client is not registred 
                client.sendall(json.dumps(str(e)).encode())
            else:
                client.sendall(json.dumps(response).encode())

        print(f'Completed requests from {address}.')
        client.close()    
        
    def run(self) -> None:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(self.address) # associate the socket with the server address.
                                    # the port is now reserved
            sock.listen() # This allows the server to listen to incoming connections.

            print(f'+ Server {self.address} running')
            while True:
                try:
                    client, address = sock.accept()
                    
                    # Starts a new thread to handle that client using __handle__
                    # Mark thread as daemon so it won't keep the process alive
                    # after the main thread receives KeyboardInterrupt.
                    t = Thread(target=self.__handle__, args=[client, address])
                    t.daemon = True
                    t.start()

                except KeyboardInterrupt:
                    print(f'- Server {self.address} interrupted')
                    break
                