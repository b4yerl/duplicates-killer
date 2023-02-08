import sys
import os

def find_duplicates(path):
  for root, dirs, files in os.walk(path):
    for file in files:
      file_path = os.path.join(root, file)
      print(open(file_path))

find_duplicates(sys.argv[1])