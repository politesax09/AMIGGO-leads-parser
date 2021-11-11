from fastapi import FastAPI
from typing import Optional

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
    fecha = getFecha(emails)
    codigo = getCodigo(emails)
    producto = getProducto(emails)
    url = getLink(emails)
    return {'fecha': fecha,
            'codigo': codigo,
            'producto': producto,
            'url': url}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}