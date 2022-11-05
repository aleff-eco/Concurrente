from threading import Condition
from time import sleep
from Receptionist import Receptionist
from Customer import Customer
from Waiter import Waiter
import queue
from Cheff import Cheff

condition = Condition()

customers = ['Rodrigo','Miranda','Héctor','Francisco','Erick','Suzana','Rogelio','Fernando',"Juana",'Maria','Daniel','Pedro','Juan','David','Maria']
max_customers = 10
max_reservations = 2

enqueue = queue.Queue()
queueTables = queue.Queue()
tables = []
order = ["", False]
reservations = queue.Queue(max_reservations)

max_waiters = 1
free_waiters = 1
requestQueue = queue.Queue()

max_cheff = 1
free_cheff = 1
foodQueue = queue.Queue()

def main():
   while True:
        print("Restaurante abierto")
        global order;
        recepcionist = Receptionist(condition)
        cheff = Cheff(condition, max_cheff, free_cheff, foodQueue)
        waiter = Waiter(condition,cheff, free_waiters , max_waiters,requestQueue)
        for customer in customers:
            customer = Customer(customer, max_customers, max_reservations,reservations,recepcionist,enqueue, tables, queueTables, waiter)
            customer.start()
            sleep(2)
        sleep(4)
        

if __name__ == '__main__':
    main()