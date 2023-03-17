from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()

def scraper(campos: dict,url):
    keys = campos.keys()
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(0.2)
    labels = driver.find_elements(by=By.CLASS_NAME, value='control-label')
    inputs = driver.find_elements(by=By.TAG_NAME,value='input')
    result = {}
    for id in set(campos.values()):
        result[id] = "-"
    # f = open("./salida.txt", "w")
    # print(json.dumps(result,indent=4))
    # raise Exception("patatas")
    for i,elem in enumerate(labels):
        if elem.text.lower() in keys:
            result[campos[elem.text.lower()]] = inputs[i].get_attribute('value')
        elif "vehicle" in keys:
            if elem.text.lower() in ('marca', 'modelo', 'version', 'potencia', 'combustible', 'cambio'):
                if len(result["vehicle"]) == 1:
                    result["vehicle"] = ''
                else: result["vehicle"] += ' | '
                result["vehicle"] += inputs[i].get_attribute('value')
    
    # f.write(json.dumps(result,indent=4))
    print(json.dumps(result, indent=4))
    return result

def scraper_hg(url):
    # diccionario {value del label: nombre de variable que espera MAKE}
    keys = {
        "codrm": "id",
        "documento": "dni",
        "fecha de nacimiento": "fchNacimiento",
        "nombre y apellidos": "nombre",
        "codigo postal": "cp",
        "uso": "uso",
        "hipoteca": "hipoteca",
        "metros construidos": "metros",
        "edificio": "tipohg",
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
        "cod presupuesto": "codPresup"

    }
    return scraper(keys,url)

def scraper_vh(url):
    keys = {
        "codrm": "id",
        "documento": "dni",
        "codigo postal": "cp",
        "fecha permiso": "fchPermiso",
        "fecha de permiso": "fchPermiso",
        "fecha de nacimiento": "fchNacimiento",
        "cod presupuesto": "codPresup",
        "tú eliges terceros ampliado + robo + incendio": "ri",
        "tú eliges terceros ampliado + lunas + robo + incendio": "rli",
        "tú eliges todo riesgo - franquicia 600": "fq600",
        "tú eliges todo riesgo - franquicia 150": "fq150",
        "terceros básico": "basica",
        "tú eliges todo riesgo - sin franquicia": "sf",
        "vehicle": "vehicle",
        "fecha 1 matriculacion": "fchMatricula",
        "1ª de matriculacion": "fchMatricula"
    }
    return scraper(keys,url)

def scraper_masc(url):
    keys = {

    }
    return scraper(keys,url)

def scraper_mt(url):
    keys = {
        "codrm": "id",
        "documento": "dni",
        "codigo postal": "cp",
        "fecha permiso": "fchPermiso",
        "fecha de permiso": "fchPermiso",
        "fecha de nacimiento": "fchNacimiento",
        "cod presupuesto": "codPresup",
        "tú eliges terceros ampliado + lunas + robo + incendio": "rli",
        "terceros básico": "basica",
        "tú eliges todo riesgo - sin franquicia": "sf",
        "vehicle": "vehicle",
        "fecha 1 matriculacion": "fchMatricula",
        "1ª de matriculacion": "fchMatricula"
    }
    return scraper(keys,url)

def scraper_sa(url):
    keys = {
        "codrm": "id",
        "documento": "dni",
        "nombre y apellidos": "nombre",
        "codigo postal": "cp",
        "número asegurados": "nAseg",
        "reembolso": "reembolso",
        "garantía bucal": "bucal",
        "asistencia sanitaria premier": "premier",
        "asistencia sanitaria supra": "supra",
        "asistencia sanitaria plus": "plus"
    }
    return scraper(keys,url)

def scraper_masc(url):
    keys = {
        "codigo postal": "cp",
        "nombre y apellidos": "dueno",
        "documento": "dni",
        "fecha de nacimiento": "fchNacimDueno",
        "codrm": "id",
        "mascota": "mascota",
        "nacimiento mascota": "fchNacimMasc",
        "pureza": "pureza",
        "raza": "raza",
        "prima tarificada1": "prima1",
        "prima tarificada2": "prima2",
        "prima tarificada3": "prima3",
        "prima tarificada4": "prima4",
        "prima tarificada5": "prima5",
        "prima tarificada6": "prima6",
    }
    return scraper(keys,url)

def scraper_all(url):
    keys = {
        # HG
        "codrm": "id",
        "documento": "dni",
        "fecha de nacimiento": "fchNacimiento",
        "nombre y apellidos": "nombre",
        "codigo postal": "cp",
        "uso": "uso",
        "hipoteca": "hipoteca",
        "metros construidos": "metros",
        "edificio": "tipohg",
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
        # VH
        "fecha permiso": "fchPermiso",
        "fecha de permiso": "fchPermiso",
        "cod presupuesto": "codPresup",
        "tú eliges terceros ampliado + robo + incendio": "ri",
        "tú eliges terceros ampliado + lunas + robo + incendio": "rli",
        "tú eliges todo riesgo - franquicia 600": "fq600",
        "tú eliges todo riesgo - franquicia 150": "fq150",
        "terceros básico": "basica",
        "tú eliges todo riesgo - sin franquicia": "sf",
        "vehicle": "vehicle",
        "fecha 1 matriculacion": "fchMatricula",
        "1ª de matriculacion": "fchMatricula",
        # SA
        "número asegurados": "nAseg",
        "reembolso": "reembolso",
        "garantía bucal": "bucal",
        "asistencia sanitaria premier": "premier",
        "asistencia sanitaria supra": "supra",
        "asistencia sanitaria plus": "plus",
        #MASC
        "mascota": "mascota",
        "nacimiento mascota": "fchNacimMasc",
        "pureza": "pureza",
        "raza": "raza",
        "prima tarificada1": "prima1",
        "prima tarificada2": "prima2",
        "prima tarificada3": "prima3",
        "prima tarificada4": "prima4",
        "prima tarificada5": "prima5",
        "prima tarificada6": "prima6"
    }
    return scraper(keys,url)
# scraper_vh('https://eur03.safelinks.protection.outlook.com/?url=http%3A%2F%2Fr.womtp.com%2Fc6sgylQIDqNPB3Td&data=05%7C01%7CMMOR31%40mediador.mapfre.com%7Cb908356f4d024106c00908dadda98c9e%7C5cc6c66dffb2469f9385cda840e57836%7C0%7C0%7C638066017524524649%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=tlzEa%2BFoUIQj4uUVbfj4Bmfq3y7IKLaCQUpHjMHD20Q%3D&reserved=0')
