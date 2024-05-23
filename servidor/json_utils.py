import json

def serialize_object(obj):
  """
  Função que serializa um objeto Python em string JSON.
  """
  return json.dumps(obj)

def deserialize_object(json_str):
  """
  Função que desserializa uma string JSON em objeto Python.
  """
  return json.loads(json_str)
