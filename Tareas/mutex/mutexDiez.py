import threading
import pytube

mutex = threading.Lock()


def get_videos(videoUrl):
    video = pytube.YouTube(videoUrl)
    video.streams.first().download("C:/VISUAL/MutexVideo")


class Hilo(threading.Thread):
    def __init__(self, videoUrl):
        threading.Thread.__init__(self)
        self.videoUrl = videoUrl

    def run(self):
        mutex.acquire()
        get_videos(self.videoUrl)
        mutex.release()


videoUrl = ["https://www.youtube.com/watch?v=JDcvtKsSfxg", "https://www.youtube.com/watch?v=4050VGwuyo0", "https://www.youtube.com/watch?v=jNQXAC9IVRw", "https://www.youtube.com/watch?v=4t91S0Cfl-4", "https://www.youtube.com/watch?v=OXLJD8z6qbg",
            "https://www.youtube.com/watch?v=I8Y_LGTnSeg", "https://www.youtube.com/watch?v=N9B9enJNqXE", "https://www.youtube.com/watch?v=gDjMZvYWUdo", "https://www.youtube.com/watch?v=4zWzA1M6XsQ", "https://www.youtube.com/watch?v=FFtYFIBqFEA"]
Hilo = [Hilo(videoUrl[0]), Hilo(videoUrl[1]), Hilo(videoUrl[2]), Hilo(videoUrl[3]), Hilo(videoUrl[4]), Hilo(
    videoUrl[5]), Hilo(videoUrl[6]), Hilo(videoUrl[7]), Hilo(videoUrl[8]), Hilo(videoUrl[9]), ]

for i in Hilo:
    i.start()
