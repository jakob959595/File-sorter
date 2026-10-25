import os
from pathlib import Path
import shutil

sourceFolder = ""

con = {}

folders = []

def create_if_not_exist(name):
    file_name = str(Path.home() / name)
    os.makedirs(file_name, exist_ok=True)
    folders.append(file_name)
    con[file_name]=[]

def add_ext(ext, folder):
    con[folder].append(ext)   

def Sort():
    files = os.listdir(sourceFolder)
    for i in files:
        split = os.path.splitext(i)
        first_path = os.path.join(sourceFolder, i)
        extention = split[1]
        for folder in con:
            for ext in con[folder]:
                if(extention == ext):
                    dest = os.path.join(folder, i)
                    os.rename(first_path, dest)











