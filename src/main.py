import sys
import os

# Ajouter le dossier src/ au PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("bonjour")
import setuptools
print(setuptools.__version__)
