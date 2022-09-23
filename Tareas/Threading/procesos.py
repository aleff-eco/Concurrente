from urllib import response
import requests
import pytube 
import mysql.connector
import time 
import threading

threading_local = threading.local()

mydb = mysql.connector.connect(
    host = "localhost",
    database = "procesos",
    user = "root",
    password = "",
)
cursor = mydb.cursor();
      
def get_service():
    r = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2020-10-25&endtime=2022-09-06&limit=2001')
    write_db(r.json())
def write_db(data):
    for i in data['features']:
        cursor.execute("INSERT INTO earthquake (title) VALUES ('" + i['properties']['title'] + "')")    
        mydb.commit()

def get_randomUser(x=0):
    response = requests.get('https://randomuser.me/api/')
    if response.status_code==200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)
        
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
    
    x=0
    for x in range(0,850):
        th1=threading.Thread(target=get_randomUser, args={x})
        th1.start()
    
    th2=threading.Thread(target=get_service) 
    th2.start()
    th3=threading.Thread(target=get_videos)
    th3.start()
    end_time = time.time() - init_time
    print(end_time)
    
    
    