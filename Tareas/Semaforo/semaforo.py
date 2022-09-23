from threading import Thread, Semaphore
from turtle import st
semaforo = Semaphore(1)

def crito(id):
    global x;
    x = x + id
    print("Hilo =" +str(id)+ " =>" + str(x))
    x=1

class Hilo(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id=id

    def run(self):
        semaforo.acquire()  # Inicializa semáforo , lo adquiere
        crito(self.id)
        semaforo.release()  # Libera un semáforo e incrementa la varibale semáforo

threads_semaphore = [Hilo(1), Hilo(2), Hilo(3)]
x=1;
for t in threads_semaphore:
    t.start()