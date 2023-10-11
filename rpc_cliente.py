import xmlrpc.client

url = "http://localhost:8000"

server = xmlrpc.client.ServerProxy(url)

peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

resultado_imc = server.calcular_imc(peso, altura)


print(f"IMC: {resultado_imc[0]}")
print(f"Classificação: {resultado_imc[1]}")
