import sys
import os
import hashlib

# Gera hash do file handler para armazenar no dict
def hash_file(file_path) :
  hash_func = hashlib.sha1()

  # Abre o arquivo como binário e faz a leitura
  with open(file_path, 'rb') as file:
    hash_func.update(file.read())
  
  return hash_func.hexdigest()

def find_duplicates(path):
  hash_table = {}

  for root, dirs, files in os.walk(path):
    for file in files:
      file_path = os.path.join(root, file)
      file_hash = hash_file(file_path)
      print(file_hash)

find_duplicates(sys.argv[1])