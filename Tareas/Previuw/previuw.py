from time import sleep
import threading
import requests

        
def get_head(url):
    #print("url "+url)
    resp = requests.head(url)
    if resp.status_code ==200:
        print(url+" Web activa| "+str(resp))
    else:
        print(url+" la solicitud no se proceso de forma correcta| "+str(resp))


class Hilo(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        h1 = threading.Thread(target=get_head, args=[self.url])
        h1.start()
    
hilos=[
    Hilo('https://ww.facebook.com/'),
    Hilo("http://pav0n.github.io/2015/05/18/recorrer-arreglos-en-python/"), 
    Hilo("https://www.youtube.com/watch?v=q7-fIS-tISs"), 
    Hilo("https://platinum.upchiapas.edu.mx/alumnos/calificaciones/index"),
    Hilo("https://classroom.google.com/u/0/c/NTI2OTYwMjIyMjA3/a/NTUwMTE4OTY1MTQw/details?hl=es"),
    Hilo("https://estudyando.com/que-es-la-prueba-de-aceptacion-del-usuario-definicion-y-ejemplos/"),
    Hilo("https://www.mercadolibre.com.mx"),
    Hilo("https://www.pinterest.com.mx"),
    Hilo("https://www.instagram.com"),
    Hilo("https://free-mp3-download.net"),
    
    Hilo("https://krispymods.com/shop/"),
    Hilo("https://krispymods.com/product/gtav-accounts/"),
    Hilo("https://translate.google.com.mx/"),
    Hilo("https://drive.google.com"),
    Hilo("https://mail.google.com"),
    Hilo("https://www.compucalitv.com/juegos-pc/dl63360750/"),
    Hilo("https://elamigos.site"),
    Hilo("https://www.reddit.com"),
    Hilo("https://www.roblox.com/home"),
    Hilo("https://www.unknowncheats.me/forum/grand-theft-auto-v/433685-kiddions-modest-external-menu.html"),
    
    Hilo("https://www.unknowncheats.me/forum/index.php"),
    Hilo("https://www.github.com/"),
    Hilo("https://www.netflix.com/"),
    Hilo("https://www.wikipedia.org/"), 
    Hilo("https://www.hbomax.com/mx/es"),]

while True:
    
    for hilo in hilos:
        hilo.start()
        #print("paso por hilos start")
    sleep(350)
        
