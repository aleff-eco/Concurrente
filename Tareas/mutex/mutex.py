from threading import Thread
import threading
from time import sleep


mutex=threading.Lock()

def crito(id):
    global x;
    x = x + id
    print("Hilo =" +str(id)+ " =>" + str(x))
    x=1


class Hilo(threading.Thread):
    
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id
        
    def run (self):
        mutex.acquire()
        #sleep(3-self.id)
        crito(self.id)
        mutex.release()
        print ("valor " + str(self.id))
        
    
    
        
hilos = [Hilo(1), Hilo(2), Hilo(3)]
x=1;
for h in  hilos: 
    h.start()