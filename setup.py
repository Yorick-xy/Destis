from setuptools import setup, find_packages

# Charger les dépendances depuis requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    
setup(
    name='Destis',               # Nom de ton projet
    version='0.1.0',                  # Version
    description='Une IA intégrée type JARVIS', 
    author='Yorick MAPET',                 
    author_email='yorick.mapet@gmail.com', 
    url='https://github.com/Yorick-xy/Destis.git', # Lien vers dépôt GitHub (si applicable)
    packages=find_packages(where='src'), # Recherche des packages dans le dossier src
    package_dir={'': 'src'},          # Déclare src comme dossier source principal
    install_requires=[                # Dépendances à installer (ou via requirements.txt)
        'numpy',
        'opencv-python',
        'speechrecognition',
        'pyttsx3',
        'paho-mqtt',
        # Si besoin ajouter ici les bibliothèques nécessaires
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',          # Version minimale de Python
)
