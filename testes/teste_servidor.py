import unittest
import socket
import json
from servidor.main import soma, fatorial

class TestServidor(unittest.TestCase):

    def setUp(self):
        # Cria um socket para simular um cliente
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.host = "localhost"
        self.port = 5000

        # Conecta ao servidor
        self.client_socket.connect((self.host, self.port))

    def tearDown(self):
        self.client_socket.close()

    def test_soma_servidor(self):
        # Envia requisição para a função "soma"
        request_json = json.dumps({"function_name": "soma", "args": [2, 3]})
        self.client_socket.sendall(request_json.encode())

        response_json = self.client_socket.recv(1024).decode()
        response_dict = json.loads(response_json)

        self.assertEqual(response_dict["result"], soma(2, 3))

    def test_fatorial_servidor(self):
        # Envia requisição para a função "fatorial"
        request_json = json.dumps({"function_name": "fatorial", "args": [5]})
        self.client_socket.sendall(request_json.encode())

        response_json = self.client_socket.recv(1024).decode()
        response_dict = json.loads(response_json)

        self.assertEqual(response_dict["result"], fatorial(5))

if __name__ == "__main__":
    unittest.main()