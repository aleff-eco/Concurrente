#clase Condiction => wait, notify y notifiAll
import threading

cond = threading.Condition()

class Client(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id
        
    def run(self):
        cond.acquire()
        cond.wait()
        data.pop()
        cond.notify()
        cond.release()
        
class Server(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        while True:
            cond.acquire()
            if len(data) != 0: cond.wait()
            data.append("data 1")
            cond.notify()
            cond.release()
        
data=[]
Client = Client()
Server = Server()

Client.start()
Server.start()

while True:
    print(data)