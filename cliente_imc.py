import xmlrpc.client
#URL
url = "http://localhost:2023"
server = xmlrpc.client.ServerProxy(url)

#Dados para calculo
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (em cm): "))
peso = float(input("Digite seu peso (em kg): "))

#Conversão
altura = altura / 100

resultado_imc = server.calculo_imc(peso, altura, idade)

imc, classificacao = resultado_imc
imc_formatado = "{:.1f}".format(imc)

#Resultado
print(f"Seu IMC é de: {imc_formatado} kg/m2")
print(f"Classificação: {classificacao}")