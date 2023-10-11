from xmlrpc.server import SimpleXMLRPCServer

#verificar se é palindromo
def palind(p):
    p = p.lower()
    p = p.replace(" ", "")

    if p == p[::-1]:
        return f"'{p}' Essa palavra é um Palíndromo."
    else:
        return f"'{p}' Essa palavra não é um Palíndromo."

#rpc
host = "localhost"
porta = 2023
server = SimpleXMLRPCServer((host, porta), allow_none=True)
server.register_function(palind, "palind")
print(f"Palindromo: {host}:{porta}")
server.serve_forever()