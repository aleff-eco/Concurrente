import pytube 
import time 
import concurrent.futures
import threading

threading_local = threading.local()

def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.submit(get_videos, url)

def get_videos():
    yt = pytube.YouTube("https://www.youtube.com/watch?v=JDcvtKsSfxg")
    yt.streams.first().download("C:/VISUAL/tube")
    yt1 = pytube.YouTube("https://www.youtube.com/watch?v=4050VGwuyo0")
    yt1.streams.first().download("C:/VISUAL/tube")
    yt2 = pytube.YouTube("https://www.youtube.com/watch?v=jNQXAC9IVRw")
    yt2.streams.first().download("C:/VISUAL/tube")
    yt3 = pytube.YouTube("https://www.youtube.com/watch?v=4t91S0Cfl-4")
    yt3.streams.first().download("C:/VISUAL/tube")
    yt4 = pytube.YouTube("https://www.youtube.com/watch?v=OXLJD8z6qbg")
    yt4.streams.first().download("C:/VISUAL/tube")
    
if __name__ == "__main__":
    init_time = time.time()
    
    th1=threading.Thread(target=get_videos)
    th1.start()
    end_time = time.time() - init_time
    print(end_time)
    