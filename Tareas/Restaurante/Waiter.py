from threading import Thread, Condition
from Customer import Customer

condition = Condition()
customerClass = Customer()

class Waiter(Thread):
    def __init__(self, condition = None, cheff= None, free_waiters = None , max_waiters= None, requestQueue= None):
        Thread.__init__(self)
        self.condition = condition
        self.cheff = cheff
        self.free_waiters = free_waiters
        self.max_waiters = max_waiters
        self.requestQueue = requestQueue
        
        
    def receiveRequest(self, customer):
        if not self.requestQueue.empty() and self.free_waiters > 0:
            self.condition.acquire()
            self.free_waiters  -= 1
            next = self.requestQueue.get()
            print(f"Mesero tomó la orden del customer {next}")
            self.cheff.cook(customer)
            self.condition.notify()
            self.condition.release()
            self.free_waiters += 1
            return next
        
        if self.free_waiters > 0: 
            self.condition.acquire()
            self.free_waiters  -= 1
            print(f"Mesero tomó la orden del customer {customer}")
            self.cheff.cook(customer)
            self.condition.notify()
            self.condition.release()
            self.free_waiters += 1
            
            return customer
        else:
            print(f"No hay meseros disponibles, la orden del {customer} esta en cola ")
            self.requestQueue.put(customer)
        
    def deliveryFood(self, customer):
        print(f"Se entrego la comida al CUSTOMER {customer}")
        customerClass.receiveFood(customer)
    
    def rest(self):
        print(f"Mesero descansado")
        

        