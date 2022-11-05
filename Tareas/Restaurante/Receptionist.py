from threading import Thread
from time import sleep


class Receptionist(Thread):
    def __init__(self, condition):
        Thread.__init__(self)
        self.condition = condition
       
        
    def reserve(self, name, max_reservations, reservations, enqueue):
        if reservations.full():
            enqueue.put(name)
            print(f"-El cliente {name} esta en COLA DE RESERVACION")
            return False
        else:
            reservations.put(name)
            print(f"-El cliente {name} esta en RESERVACION")
            return True
    
    def giveTable(self, name, is_reserved, max_customers, reservations, enqueue, queueTables, tables):
        self.condition.acquire()
        in_table = False
        if len(tables)  < max_customers and is_reserved:
            tables.append(name)
            print(f"-El cliente {name} esta en SU MESA POR RESERVACION")
            in_table = True
        elif len(tables) < max_customers-2:
            tables.append(name)
            print(f"-El cliente {name} esta en SU MESA")
            in_table = True
        else:
            queueTables.put(name)
            print(f"-El cliente {name} esta en COLA DE MESAS")
            in_table = False
        self.condition.notify()
        self.condition.release()
        return in_table