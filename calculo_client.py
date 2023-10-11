import xmlrpc.client
#url
url = "http://localhost:2023"
server = xmlrpc.client.ServerProxy(url)

#Dados para calculo
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

#Resultado
resultado = server.calc_equacao(a, b, c)
for eq in resultado:
    print(eq)
