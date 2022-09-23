#callback
from urllib import response
import requests
import threading


def get_service1(response_json_data):
    print(response_json_data)

def get_error1():
    print("error en la solicitud")
    
def get_service2(response_json_data):
    print(response_json_data)

def get_error2():
    print("error en la solicitud")

def request_data(url, success_callback, error_callback):
    response = requests.get(url)
    if response.status_code == 200:
        success_callback(response.json())
    else:
        error_callback()



class Hilo(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
                                  
    def run(self):
        h1 = threading.Thread(target=request_data,
        kwargs={
            'url':'',
            'sucess_callback': get_service1, 
            'error_callback': get_error1
        })
        h1.start()
        
        h2 = threading.Thread(target=request_data,
        kwargs={
            'url':'',
            'sucess_callback': get_service2, 
            'error_callback': get_error2
        })
        h2.start()
hilo= Hilo()
hilo.start()