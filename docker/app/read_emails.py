from bs4 import BeautifulSoup
import re
from myhttp import send_post
from py_scraper.scraper import *
import traceback
import urllib


# Define the SCOPES. If modifying it, delete the token.pickle file.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def handle_email(content):
    print("ESTO ES MIO: \n\n\n\n\n")
    print(content)
    soup = BeautifulSoup(content,"html.parser")

    results = {}
    for elem in soup.find_all("li"):
        if "fecha" in elem.text.lower():
            results["fecha"] = elem.text.split(": ")[1]
        elif "código" in elem.text.lower():
            results["codigo"] = elem.text.split(": ")[1]
        elif "producto" in elem.text.lower():
            results["tipo"] = elem.text.split(": ")[1]

    links = soup.find_all("a")
    ok = False

    for elem in links:
        try:
            results["url"] = elem.attrs["href"].split("url=")[1].split("&")[0]
            break
        except:
            pass

    # results["url"] = soup.find_all("a").attrs["href"].split("url=")[1].split("&")[0]

    result = None
    make_route = ""
    if results["tipo"].lower() == "coche":
        result = scraper_vh(results["url"])
        make_route = "https://hook.eu1.make.com/05fhvgdyc310mrhio7b594tmxgh2oh08"
    elif results["tipo"].lower() == "hogar":
        result = scraper_hg(results["url"])
        make_route = "https://hook.eu1.make.com/3x26j8yf7gexv7oifp51tljymo3579xx"
    elif results["tipo"].lower() == "salud":
        result = scraper_sa(results["url"])
        make_route = "https://hook.eu1.make.com/8xqg35u5dolbrtxs6t2hsd5tf34aauo7"
    elif results["tipo"].lower() == "moto":
        result = scraper_mt(results["url"])
        make_route = "https://hook.eu1.make.com/1jwc474jipjwc1v5zrbhzo80kza2misd"
    elif results["tipo"].lower() == "mascotas":
        result = scraper_masc(results["url"])
        make_route = "https://hook.eu1.make.com/atqnslps9ekqwm6owaxa9mgvyh2iz55g"
    elif results["tipo"] == "*":
        result = scraper_all(results["url"])
        make_route = "https://hook.eu1.make.com/7ktuy7bxoqxgy86v5o4d3w58dw8secsr"
    else:
        print("No nos hacemos responsables")

    result.update(results)
    print(result)
    send_post(make_route,result)
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
    try:
        index = soup.find('Código: ') + 8
        index2 = soup.find(' ', index)
        return soup
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
        tagStr = soup.split("url=3D")
        link = "patatas" 
        tagStr = tagStr[1]
        link = urllib.parse.unquote(tagStr.split("&")[0])
        # link = link[link.rfind('&')+5:]
        print(f"[[[[[{link}]]]]]")
        return link.replace("\r","").replace("\n","").replace("=","")
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