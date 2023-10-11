from xmlrpc.server import SimpleXMLRPCServer

def calc_imc(peso, altura, idade):
    imc = peso / (altura ** 2)

#Calculo do IMC
    if imc < 18.5:
        mensagem = "Magreza"
    elif 18.5 <= imc < 24.9:
        mensagem = "Normal"
    elif 24.9 <= imc < 29.9:
        mensagem = "Sobrepeso"
    else:
        mensagem = "Obesidade"

    return imc, mensagem

#RPC
host = "localhost"
porta = 2023
server = SimpleXMLRPCServer((host, porta), allow_none=True)
server.register_function(calc_imc, "calculo_imc")
print(f"Calculo IMC: {host}:{porta}")
server.serve_forever()