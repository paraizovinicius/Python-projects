from rpc import RPCServer

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

server = RPCServer()

server.registerMethod(add)
server.registerMethod(sub)
server.registerMethod(multiply)
server.registerMethod(divide)

server.run()