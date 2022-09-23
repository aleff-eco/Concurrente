import requests
import time
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    database = "pruebasin",
    user = "root",
    password = "",
)
cursor = mydb.cursor();


def get_name():
    r = requests.get('https://randomuser.me/api/?results=200')

    if r.status_code == 200:
        results = r.json().get('results')
        for name in results:  
            write_db(name['name']['first'])
            

def write_db(x):
    cursor.execute("INSERT INTO user(name) VALUES('"+x+"')")
    mydb.commit()    


if __name__ == "__main__":
    start_time = time.time()
    get_name()
    end_time = time.time()
    print(end_time - start_time)