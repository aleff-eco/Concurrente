from threading import Thread, Semaphore
from turtle import st
import pytube
semaforo = Semaphore(1)

def get_videos(videoUrl):
    video = pytube.YouTube(videoUrl)
    video.streams.first().download("C:/VISUAL/SemaforoVideo")
    
class Hilo(Thread):
    def __init__(self, videoUrl):
        Thread.__init__(self)
        self.videoUrl = videoUrl
        
    def run(self):
        semaforo.acquire()  # Inicializa semáforo , lo adquiere
        get_videos(self.videoUrl)
        semaforo.release()  # Libera un semáforo e incrementa la varibale semáforo

videoUrl=["https://www.youtube.com/watch?v=JDcvtKsSfxg","https://www.youtube.com/watch?v=4050VGwuyo0","https://www.youtube.com/watch?v=jNQXAC9IVRw","https://www.youtube.com/watch?v=4t91S0Cfl-4","https://www.youtube.com/watch?v=OXLJD8z6qbg","https://www.youtube.com/watch?v=I8Y_LGTnSeg","https://www.youtube.com/watch?v=N9B9enJNqXE","https://www.youtube.com/watch?v=gDjMZvYWUdo","https://www.youtube.com/watch?v=4zWzA1M6XsQ","https://www.youtube.com/watch?v=FFtYFIBqFEA"]    

threads_semaphore = [Hilo(videoUrl[0]), Hilo(videoUrl[1]),Hilo(videoUrl[2]),Hilo(videoUrl[3]),Hilo(videoUrl[4]),Hilo(videoUrl[5]),Hilo(videoUrl[6]),Hilo(videoUrl[7]),Hilo(videoUrl[8]),Hilo(videoUrl[9]),]

for t in threads_semaphore:
    t.start()
