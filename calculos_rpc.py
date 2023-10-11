from xmlrpc.server import SimpleXMLRPCServer

#Equação 2º Grau
def calc_equacao(a, b, c):
    if a == 0:
        return ["O coeficiente 'a' não pode ser zero."]
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        return ["Possuem duas raízes:", x1, x2]
    elif delta == 0:
        x1 = -b / (2 * a)
        return ["Possui uma raiz:", x1]
    else:
        return ["Não tem raíz real"]

#RPC
host = "localhost"
porta = 2023
server = SimpleXMLRPCServer((host, porta), allow_none=True)
server.register_function(calc_equacao, "calc_equacao")
print(f"Calculo Equação 2º Grau: {host}:{porta}")
server.serve_forever()
