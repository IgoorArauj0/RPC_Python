import xmlrpc.client

url = "http://localhost:2023"
server = xmlrpc.client.ServerProxy(url)
p = input("Digite uma palavra: ")

result = server.palind(p)
print(result)
