#Este servidor NameServer
#Prorciona un namespace en Redis
#Por cada id de chat este servidor tiene que prorcionar los parametros de conexión
#Los ids de los chats son nombres de usuario para chats privados
# y nombres de grupos para chats grupales.
#Al conectarse directamente a un chat, los clientes deben pedir al servidor su dirección
# para establecer la conexión correspondiente.
#Al iniciarse, los clientes registrarán automáticamente su dirección IP y su puerto
# en el servidor de nombres, asociados a su nombre de usuario.
#
import grpc
from concurrent import futures
import metods
import time
import redis

import NameServer_pb2_grpc
import NameServer_pb2

from metods import metods

class NameServerServiceServicer(NameServer_pb2_grpc.NameServerServiceServicer):

    def test(self, empty, context):
        text = metods.test()
        response = NameServer_pb2.testResponse()
        response.sentence=text
        print(f"Response data: {text}")  # Add this line
        return response

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

NameServer_pb2_grpc.add_NameServerServiceServicer_to_server(
    NameServerServiceServicer(), server)

r = redis.Redis(host='localhost', port=6379)
# listen on port 50051
server.add_insecure_port('0.0.0.0:50051')
server.start()
print('Starting server. Listening on port 50051.')


# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

