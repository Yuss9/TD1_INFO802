from zeep import Client

# implémenter un client qui interroge votre service
client = Client('http://localhost:8000/?wsdl')
print(client.service.say_hello('Jean', 5))
print(client.service.addition(1.5, 2.5))
