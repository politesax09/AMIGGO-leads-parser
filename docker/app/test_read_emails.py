from docker.app.read_emails import *
# from read_emails import *

emails = getEmails()
fecha = getFecha(emails)
codigo = getCodigo(emails)
producto = getProducto(emails)
url = getLink(emails)

fechareg = getFechaReg(emails)
codigoreg = getCodigoReg(emails)

# print(fecha)
# print(codigo)
# print(producto)
# print(url)

print(fechareg)
print(codigoreg)