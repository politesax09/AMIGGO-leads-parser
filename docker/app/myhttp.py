import requests

def send_post(data):
    return requests.post('https://hook.eu1.make.com/hdoejxsnprje036necx8o5413rcd4m7h', json=data)