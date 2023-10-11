from xmlrpc.server import SimpleXMLRPCServer
import math

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        mensagem = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        mensagem = "Peso normal"
    elif 24.9 <= imc < 29.9:
        mensagem = "Sobrepeso"
    else:
        mensagem = "Obesidade"

    return imc, mensagem


host = "localhost"
porta = 8000

server = SimpleXMLRPCServer((host, porta), allow_none=True)

server.register_function(calcular_imc, "calcular_imc")

print(f"Servidor RPC IMC rodando em {host}:{porta}")
server.serve_forever()
