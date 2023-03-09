from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time

def scraper(campos: dict,url):
    keys = campos.keys()
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(0.2)
    labels = driver.find_elements(by=By.CLASS_NAME, value='control-label')
    inputs = driver.find_elements(by=By.TAG_NAME,value='input')
    result = {}
    if "vehicle" in keys:
        result["vehicle"] = "-"
    for i,elem in enumerate(labels):
        if elem.text.lower() in keys:
            result[campos[elem.text.lower()]] = inputs[i].get_attribute('value')
        elif "vehicle" in keys:
            if elem.text.lower() in ('marca', 'modelo', 'version', 'potencia', 'combustible', 'cambio'):
                if len(result["vehicle"]) == 1:
                    result["vehicle"] = ''
                else: result["vehicle"] += ' | '
                result["vehicle"] += inputs[i].get_attribute('value')
    
    print(json.dumps(result, indent=4))

def scraper_hg(url):
    keys = {
        "codrm": "id",
        "documento": "dni",
        "fecha de nacimiento": "fechaNacimiento",
        "nombre y apellidos": "nombre",
        "codigo postal": "cp",
        "uso": "uso",
        "hipoteca": "hipoteca",
        "metros construidos": "metros",
        "edificio": "tipo",
        "año construccion": "anoConst",
        "anio construccion": "anoConst",
        "capital contenido propuesto": "contenido",
        "capital continente propuesto": "continente",
        "referencia nse tú eliges": "codBas",
        "referencia nse familia": "codFam",
        "referencia nse platino": "codPlat",
        "modalidad tú eliges": "hb",
        "hogar basico": "hb",
        "modalidad familiar": "hf",
        "hogar familiar": "hf",
        "modalidad platino": "hp",
        "hogar platino": "hp",
        "modalidad total": "ht",
        "hogar total": "ht",
    }
    scraper(keys,url)

def scraper_vh(url):
    keys = {
        "codrm": "id",
        "documento": "dni",
        "codigo postal": "cp",
        "fecha permiso": "fechaPermiso",
        "fecha de permiso": "fechaPermiso",
        "fecha de nacimiento": "fechaNacimiento",
        "cod presupuesto": "codPresup",
        "tú eliges terceros ampliado + robo + incendio": "ri",
        "tú eliges terceros ampliado + lunas + robo + incendio": "rli",
        "tú eliges todo riesgo - franquicia 600": "fq600",
        "tú eliges todo riesgo - franquicia 150": "fq150",
        "terceros básico": "basica",
        "tú eliges todo riesgo - sin franquicia": "sf",
        "vehicle": "vehicle",
        "fecha 1 matriculacion": "matricula",
        "1ª de matriculacion": "matricula"
    }
    scraper(keys,url)

scraper_vh('https://eur03.safelinks.protection.outlook.com/?url=http%3A%2F%2Fr.womtp.com%2Fc6sgylQIDqNPB3Td&data=05%7C01%7CMMOR31%40mediador.mapfre.com%7Cb908356f4d024106c00908dadda98c9e%7C5cc6c66dffb2469f9385cda840e57836%7C0%7C0%7C638066017524524649%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=tlzEa%2BFoUIQj4uUVbfj4Bmfq3y7IKLaCQUpHjMHD20Q%3D&reserved=0')