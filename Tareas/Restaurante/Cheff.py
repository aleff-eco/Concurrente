from threading import Thread
from Waiter import Waiter

waiter = Waiter()

class Cheff(Thread):
    def __init__(self, condition, max_cheff, free_cheff, foodQueue):
        Thread.__init__(self)
        self.condition = condition
        self.max_cheff = max_cheff
        self.free_cheff = free_cheff
        self.foodQueue = foodQueue
        
        
    def cook(self, customer):
        if not self.foodQueue.empty() and self.free_cheff > 0:
            self.condition.acquire()
            self.free_cheff  -= 1
            next = self.foodQueue.get()
            print(f"Cheff cocino la comida de {next}")
            waiter.deliveryFood(next)
            self.condition.notify()
            self.condition.release()
            self.free_cheff += 1
        
        if self.free_cheff > 0: 
            self.condition.acquire()
            self.free_cheff  -= 1
            print(f"Cheff cocino la comida de {customer}")
            waiter.deliveryFood(customer)
            self.condition.notify()
            self.condition.release()
            self.free_cheff += 1
        else:
            print(f"No hay cheffs disponibles, la orden del {customer} esta en cola ")
            self.foodQueue.put(customer)
        
    