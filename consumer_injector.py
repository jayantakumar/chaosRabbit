import requests
import json
from requests.auth import HTTPBasicAuth
from xmlrpc.server import SimpleXMLRPCServer

server = SimpleXMLRPCServer(('localhost',3001),logRequests=True)

class ConsumerInjector:
    def __init__(self) -> None:   
        self.consumers_pid = []

    def putPids(self,p):
        self.consumers_pid = p
        print(p)
        return ""

    def getPids(self):
        return self.consumers_pid

    def killProcess(self,pid):
        command1 = f"kill -STOP {pid}"
        import os
        try:
            os.system(command1)

            return "Success"
        except:
            print("Exception occured")
            return Exception("Exception Occured")
        
    def resumeProcess(self,pid):
        command2 = f"kill -CONT {pid}"
        import os
        try:
            os.system(command2)

            return "Success"
        except:
            print("Exception occured")
            return Exception("Exception Occured")
        


server.register_instance(ConsumerInjector())
if __name__=="__main__":
    try:
        print("Serving..")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting..")