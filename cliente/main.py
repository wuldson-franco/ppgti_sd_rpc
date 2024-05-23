import socket
import json

# Define endereço e porta do servidor
host = "localhost"
port = 5000

# Cria socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecxão
client_socket.connect((host, port))
print(f"Conectado ao servidor {host}:{port}")

# Função para enviar requisições RPC
def send_request(function_name, args):
  """
  Função que envia uma requisição RPC para o servidor.
  """
# Converte a requisição em string JSON
  request_dict = {"function_name": function_name, "args": args}
  request_json = json.dumps(request_dict)

  # Envia a requisição para o servidor
  client_socket.sendall(request_json.encode())

 
  response_json = client_socket.recv(1024).decode()
  response_dict = json.loads(response_json)

 
  if "result" in response_dict:
    return response_dict["result"]
  else:
    raise Exception(response_dict["error"])

# Testando
result = send_request("soma", [2, 3])
print("Soma:", result)

result = send_request("fatorial", [5])
print("Fatorial:", result)


client_socket.close()
print("Conexão encerrada")