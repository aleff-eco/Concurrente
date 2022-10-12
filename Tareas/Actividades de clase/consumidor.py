from threading import Thread 
import threading
import time, random
import queue

bodega = queue.Queue(maxsize=20)

class Productor(Thread):
    def __init__(self, bodega):
        threading.Thread.__init__(self)
        self.bodega = bodega

    def run(self):
        while True:
            if not self.bodega.full():
                array1 = random.randint(0, 20)
                self.bodega.put(array1)
                print("Se agrego un nuevo intem: " + str(array1))
                time.sleep(5)

class Consumidor(Thread):
    def __init__(self, bodega):
        threading.Thread.__init__(self)
        self.bodega=bodega
        
        
    def run(self):
        while True:
            if not self.bodega.empty():
                producto = self.bodega.get()
                print("Consumidor toma producto: " + str(producto))
                
                time.sleep(5)
     
    




def main():
    hilo_productor = Productor(bodega)
    hilo_consumidor = Consumidor(bodega)

    hilo_productor.start()
    hilo_consumidor.start()


main()
