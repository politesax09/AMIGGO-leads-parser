# import the required libraries
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
import pickle
import os.path
import base64
# import email
from bs4 import BeautifulSoup
import re
from myhttp import send_post
from py_scraper.scraper import *
import traceback
import urllib


# Define the SCOPES. If modifying it, delete the token.pickle file.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def handle_email(content):
    soup = BeautifulSoup(content,"html.parser")
    codigo = getCodigo(soup)
    url = getLink(content)
    print('URL: ', url)
    if codigo != 'null' and url != 'null':
        fecha = getFecha(soup)
        producto = getProducto(content)
    else:
        fecha = 'null'
        producto = 'null'
    # print(producto)
    # TODO:
    # - escuchar emails -> Recibir email (cambiar servidor API por servidor de correo)
    # - Parsear email (id, tipo, url)
    # - Ejecutar tarea APIFY (traducir js a python)
    # - Traducir JSON output y enviar petición a make
    #       Es una peticion POST con el JSON de todos los datos del lead
    if producto.lower() == "coche":
        scraper_vh(url)
    elif producto.lower() == "hogar":
        scraper_hg(url)
    elif producto.lower() == "salud":
        scraper_sa(url)
    elif producto.lower() == "moto":
        scraper_mt(url)
    elif producto.lower() == "mascotas":
        scraper_masc(url)
    elif producto == "*":
        scraper_all(url)
    else:
        print("No nos hacemos responsables")
    # send_post({'fecha': fecha,
    #         'id': codigo,
    #         'tipo': producto,
    #         # coche, hogar, salud, moto, mascotas, *
    #         'url': url})



# def getEmails():
#     # Variable creds will store the user access token.
#     # If no valid token found, we will create one.
#     creds = None

#     # The file token.pickle contains the user access token.
#     # Check if it exists
#     if os.path.exists('token.pickle'):
#         # Read the token from the file and store it in the variable creds
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)

#     # If credentials are not available or are invalid, ask the user to log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file('credentials_old.json', SCOPES)
#             creds = flow.run_local_server(port=0)

#         # Save the access token in token.pickle file for the next run
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)

#     # Connect to the Gmail API
#     service = build('gmail', 'v1', credentials=creds)

#     # request a list of all the messages
#     result = service.users().messages().list(maxResults=1, userId='me').execute()

#     # We can also pass maxResults to get any number of emails. Like this:
#     # result = service.users().messages().list(maxResults=200, userId='me').execute()
#     messages = result.get('messages')

#     # messages is a list of dictionaries where each dictionary contains a message id.

#     # iterate through all the messages
#     for msg in messages:
#         # Get the message from its id
#         txt = service.users().messages().get(userId='me', id=msg['id']).execute()

#         # Use try-except to avoid any Errors
#         try:
#             # Get value of 'payload' from dictionary 'txt'
#             payload = txt['payload']
#             headers = payload['headers']

#             # Look for Subject and Sender Email in the headers
#             for d in headers:
#                 if d['name'] == 'Subject':
#                     subject = d['value']
#                 if d['name'] == 'From':
#                     sender = d['value']

#             # The Body of the message is in Encrypted format. So, we have to decode it.
#             # Get the data and decode it with base 64 decoder.
#             parts = payload.get('parts')[0]
#             data = parts['body']['data']
#             data = data.replace("-", "+").replace("_", "/")
#             decoded_data = base64.b64decode(data)

#             # Now, the data obtained is in lxml. So, we will parse
#             # it with BeautifulSoup library
#             soup = BeautifulSoup(decoded_data, "html.parser")

#         except:
#             pass

#     return soup


def getFecha(soup):
    soupStr = str(soup)
    try:
        index = soupStr.find('Fecha registro:') + 15
        return (soupStr[index:index+11]).strip()
    except:
        return 'null'

def getCodigo(soup):
    soupStr = str(soup)
    try:
        index = soupStr.find('Código: ') + 8
        index2 = soupStr.find(' ', index)
        return (soupStr[index:index2]).strip()
    except:
        return 'null'

def getProducto(soup: str):
    # soupStr = str(soup)
    # li_list = soup.find_all('li')
    # print(soup)
    # print(f"producto: {li_list}")
    segment = "".join(soup.split("li")[1:-1]).lower()
    if "coche" in segment:
        return "coche"
    elif "hogar" in segment:
        return "hogar"
    elif "salud" in segment:
        return "salud"
    elif "moto" in segment:
        return "moto"
    elif "mascotas" in segment:
        return "mascotas"
    elif "*" in segment:
        return "*"

    # try:
    #     index = soupStr.find('Producto:') + 10
    #     index2 = soupStr.find(' ', index)
    #     return (soupStr[index:index2]).strip()
    # except:
    #     return 'null'

def getLink(soup):
    try:
        print("empezamos...")
        # print(soup.find_all('a'))
        # tag = soup.find_all('a')[0]
        # print(soup)
        tagStr = soup.split("url=3Dh=")
        link = "patatas"
        print(f"le tamañé {len(tagStr)}")
        if len(tagStr) < 2:
            tagStr = soup.split("url=3D")
            tagStr = tagStr[1]
            link = urllib.parse.unquote(tagStr.split("&")[0])
        else:
            tagStr = tagStr[1]
            link = urllib.parse.unquote("h"+tagStr[2:].split("&")[0])
        # link = link[link.rfind('&')+5:]
        print(f"[[[[[{link}]]]]]")
        return link
    except:
        print("Hemos petao")
        traceback.print_exc()
        return 'null'

# def get_link(soup):
#     try:
#         tag = soup.find_all('a')

def getFechaReg(soup):
    soupStr = str(soup)
    try:
        match = re.search('Fecha registro:',soupStr)
        if match:
            index = match.end() + 1
            return (soupStr[index:index+11]).strip()
    except:
        return 'null'

def getCodigoReg(soup):
    soupStr = str(soup)
    try:
        match = re.search('Código: ')
        if match:
            index = match.end()
            index2 = soupStr.find(' ', index)
            return (soupStr[index:index2]).strip()
    except:
        return 'null'