import requests
from bs4 import BeautifulSoup

def scraper_vh(url):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    print(soup.prettify())

    # Datos cliente
    print(soup.find('label', {'class':'control-label'}))
    
    

    # return {
    #     'id': id,
    #     'dni': dni,
    #     'cp': cp,
    #     'fechaPermiso': fechaPermiso,
    #     'fechaNacimiento': fechaNacimiento,
    #     'codPresup': codPresup,
    #     'ri': ri,
    #     'rli': rli,
    #     'fq600': fq600,
    #     'fq150': fq150,
    #     'basica': basica,
    #     'sf': sf,
    #     'vehicle': vehicle,
    #     'matricula': fechaMatricula
    # }



scraper_vh('https://eur03.safelinks.protection.outlook.com/?url=http%3A%2F%2Fr.womtp.com%2Fc6sgylQIDqNPB3Td&data=05%7C01%7CMMOR31%40mediador.mapfre.com%7Cb908356f4d024106c00908dadda98c9e%7C5cc6c66dffb2469f9385cda840e57836%7C0%7C0%7C638066017524524649%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=tlzEa%2BFoUIQj4uUVbfj4Bmfq3y7IKLaCQUpHjMHD20Q%3D&reserved=0')