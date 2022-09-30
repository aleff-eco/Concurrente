import threading


mutex=threading.Lock()

def usar(persona):
    print("La persona "+(str(persona))+" esta usado el palillo." )


class persona(threading.Thread):
    
    def __init__(self, persona):
        threading.Thread.__init__(self)
        self.persona=persona
        
    def run (self):
        mutex.acquire()
        usar(self.persona)
        print ("Persona " + str(self.persona)+" acabo de comer.")
        mutex.release()
        
Personas = [persona(1), persona(2), persona(3), persona(4), persona(5), persona(6), persona(7), persona(8)]
for h in  Personas: 
    h.start()