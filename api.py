from fastapi import FastAPI
from read_emails import getEmails, getFecha, getCodigo, getProducto, getLink

app = FastAPI()

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
