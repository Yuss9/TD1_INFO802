from spyne import Application, rpc, ServiceBase, \
    Integer, Unicode, Decimal
from spyne import Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import decimal
from wsgiref.simple_server import make_server


class HelloWorldService(ServiceBase):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def say_hello(ctx, name, times):
        for i in range(times):
            yield u'Hello, %s' % name
    # def function addition

    @rpc(Decimal, Decimal, _returns=Decimal)
    def addition(ctx, a, b):
        return a+b


application = Application([HelloWorldService], 'spyne.examples.hello.soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())
wsgi_application = WsgiApplication(application)


# 5. Il reste à instancier un serveur web (dans un main):
if __name__ == '__main__':
    # 6. Instanciation et lancement du serveur:
    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()
