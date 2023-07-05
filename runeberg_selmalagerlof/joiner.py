import json
import os
import re
from pathlib import Path

input_file = os.path.join(os.path.dirname(__file__), 'runeberg_selmalagerlof_books.json')

with open(input_file) as json_file:
    books = json.load(json_file)
    with open("/wrk/nanoGPT/data/runeberg_selmalagerlof/input.txt", "w") as join_file:
      for book in books:
        name = Path("./"+book["name"]+".txt")
        with open(name) as file:
          for line in file:
            join_file.write(line)
          join_file.write("\n")
