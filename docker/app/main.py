from fastapi import FastAPI
#from typing import Optional

from read_emails import getEmails, getFecha, getCodigo, getProducto, getLink



app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/hello')
def hello():
    return 'Hello'

@app.get('/last-email')
def lastemail():
    emails = getEmails()
    codigo = getCodigo(emails)
    url = getLink(emails)
    if codigo != 'null' and url != 'null':
        fecha = getFecha(emails)
        producto = getProducto(emails)
    else:
        fecha = 'null'
        producto = 'null'
    return {'fecha': fecha,
            'codigo': codigo,
            'producto': producto,
            'url': url}

