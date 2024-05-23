import socket
import json
from . import json_utils

# Definição de funções remotas
def soma(a, b):
  return a + b

def fatorial(n):
  if n < 0:
    return 1
  else:
    return n * fatorial(n - 1)

# Cria socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "localhost"
port = 5000

# Juntando o socket ao endereço e porta
server_socket.bind((host, port))

# Número máximo de clientes em espera
server_socket.listen(5)

print(f"Servidor escutando em {host}:{port}")

while True:
  # Aceitando uma nova conexão
  (client_socket, client_address) = server_socket.accept()
  print(f"Nova conexão de {client_address}")

  request_json = client_socket.recv(1024).decode()
  request_dict = json.loads(request_json)

  function_name = request_dict["function_name"]
  args = request_dict["args"]

  # Tenta executar a função com os argumentos recebidos
  try:
    if function_name == "soma":
      result = soma(*args)
    elif function_name == "fatorial":
      result = fatorial(*args)
    else:
      raise Exception(f"Função não encontrada: {function_name}")

    response_json = json.dumps({"result": result})

    client_socket.sendall(response_json.encode())

  except Exception as e:
    error_json = json.dumps({"error": str(e)})
    client_socket.sendall(error_json.encode())

  client_socket.close()
  print(f"Conexão com {client_address} encerrada")