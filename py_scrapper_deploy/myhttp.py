import requests

def send_post(url,data):
    return requests.post(url, data=data)