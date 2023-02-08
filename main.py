import sys
import os
import hashlib

def find_duplicates(path):
  hash_table = {}

  for root, dirs, files in os.walk(path):
    for file in files:
      file_path = os.path.join(root, file)
      file_hash = hash_file(file_path)
      hasKey = hash_table.get(file_hash)
      
      # Verifica se já existe uma key com o mesmo hash
      if hasKey:
        kill_duplicate(file_path)
      else:
        hash_table.update({file_hash: file_path})
  print('\nNo more duplicates\n')

# Gera hash do file handler para armazenar no dict
def hash_file(file_path) :
  hash_func = hashlib.sha1()

  # Abre o arquivo como binário e faz a leitura
  with open(file_path, 'rb') as file:
    hash_func.update(file.read())
  
  return hash_func.hexdigest()

def kill_duplicate(path):
  print('\n--DUPLICATE FOUND AT--\n')
  print(path)
  user_decision = input('\nDo you want to remove it? (y/n): ')

  # Confere se o input é válido
  while user_decision.lower() not in ['y', 'n']:
    user_decision = input('Please insert y or n: ')
  
  # Remove ou conserva o arquivo duplicado
  if(user_decision.lower() == 'y'):
    os.remove(path)
    print('\n--FILE REMOVED--')
  else:
    print('\n--KEEP FILE--')


# Verifica os command-line arguments
if(len(sys.argv) > 1):
  find_duplicates(sys.argv[1])
else:
  print('Please provide a root directory')