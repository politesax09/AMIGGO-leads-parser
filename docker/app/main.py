from fastapi import FastAPI
#from typing import Optional

from read_emails import getEmails, getFecha, getCodigo, getProducto, getLink

# MONJE PASTILLERO: Apunta un control de errores q avise por correo ya q estamos, Se me ocurre

# TODO:
# - escuchar emails -> Recibir email (cambiar servidor API por servidor de correo)
# - Parsear email (id, tipo, url)
# - Ejecutar tarea APIFY (traducir js a python)
# - Traducir JSON output y enviar petición a make
#       Es una peticion POST


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

@app.get('/last-email2')
def lastemail2():
    return {'fecha':'2021-11-26 08:02:09',
            'codigo': '6531787',
            'producto': 'Hogar',
            'url':'https://apps.walmeric.com/clients/custom/mapfre/rm/20211129/?clientHash=28945f94d414949bf95fb2e6109142cfef1fb2a78114c2c536a36bf5a65b953abe4cb254380fee21da1e87e8c82a173c2256c0940ada1f402a8e36cb8005bad3c42fab8ae8e2f8d511d907204b5b78f7e3c6ad2802809f6f278c6e1ac928d48be43f94c9413d24187f5e8c03a2ed269d&leadId=425d1d1c409dc616a325063a4e7721e565266595&ownerId=75bfb58ff1b0a0197a127f733170910b'}
