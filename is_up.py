from sys import argv
from os import system
import re

response = system ("ping -n  1 "+ argv[1] + " > nul")

if not re.search (r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", argv[1]):
    print("addresse ip pas bonne")
elif response == 0:
    print(f"UP !")
else:
    print(f"DOWN !")