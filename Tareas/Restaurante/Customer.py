import random
from time import sleep
from threading import Condition, Thread

class Customer(Thread):
    def __init__(self, customer=None,max_customers=None, max_reservations=None, reservations=None, recepcionist=None,enqueue=None, tables=None, queueTables=None, waiter=None):
        Thread.__init__(self)
        self.customer = customer
        self.max_customers = max_customers
        self.max_reservations = max_reservations
        self.reservations = reservations
        self.recepcionist = recepcionist
        self.condition = Condition()
        self.enqueue = enqueue
        self.tables = tables
        self.queueTables = queueTables
        self.waiter = waiter
        self.in_table = False
        self.is_reserved = 0
        self.end = ''
        
    
    def talkWithRecepcionist(self, customer, is_reserved):
        self.in_table = self.recepcionist.giveTable(customer, is_reserved, self.max_customers, self.reservations, self.enqueue, self.queueTables, self.tables)
        
    def reserve(self):
        self.arriving = self.recepcionist.reserve(self.customer, self.max_reservations, self.reservations, self.enqueue)
    
    def requestFood(self):
        self.end = self.waiter.receiveRequest(self.customer)
        
    def receiveFood(self,customer):
        print(f"CUSTOMER {customer} esta comiendo")
        sleep(random.randint(1,3))
    
    def run(self):
        print(f"Cliente: {self.customer} ")
        reserva = random.randint(0,1)
        self.is_reserved = reserva
        if reserva == 1: 
            self.reserve() 
            while self.arriving == True:
                
                self.condition.acquire()
                sleep(random.randint(5,6))
                customer = self.reservations.get()
                if not self.enqueue.empty():
                    next = self.enqueue.get()
                    self.reservations.put(next)
                if len(self.tables) < self.max_customers:
                    self.talkWithRecepcionist(customer, 1)
                else:
                   self.queueTables.put(customer)   
                self.condition.notify()
                self.condition.release()  
                
        if reserva == 0:
            self.talkWithRecepcionist(self.customer, 0)
            
        if self.in_table:
            self.requestFood()
            
        for table in self.tables:
            if table == self.end:
                self.tables.remove(self.end)
           
        if not self.tables:
            self.waiter.rest()         
                
        
        
        
        

        
        
        
        
    