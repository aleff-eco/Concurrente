import requests
import mysql.connector
import time 
import concurrent.futures
import threading

threading_local = threading.local()

mydb = mysql.connector.connect(
    host = "localhost",
    database = "prueba05de09",
    user = "root",
    password = "",
)
cursor = mydb.cursor();

def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service, url)
        
def get_service():
    r = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2015-10-25&endtime=2018-09-06&limit=5000')
    write_db(r.json())
    pass 
def write_db(data):
    for i in data['features']:
        #print(i)  
        cursor.execute("INSERT INTO earthquake (title) VALUES ('" + i['properties']['title'] + "')")    
        mydb.commit()       
    pass


if __name__ == "__main__":
    init_time = time.time()
    get_service()
    end_time = time.time() - init_time
    print(end_time)
    
    