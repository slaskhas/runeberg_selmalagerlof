"""Project Runeberg - Selma Lagerlöf : Download and cleanup of Dataset."""

import json
import shutil
import tempfile
import urllib.request
from zipfile import ZipFile
import os
import re
from pathlib import Path


_DESCRIPTION = """\
Project Runeberg (runeberg.org) is a volunteer effort to create free \
electronic editions of classic Nordic (Scandinavian) literature \
and make them openly available over the Internet. \
This dataset is by Lagerlöf, Selma (1858–1940), writer, Sweden.
"""

CLEANR = re.compile('<.*?>')


def zipdownloader(src):
    
    with urllib.request.urlopen(src) as response:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(response, tmp_file)

    with open(tmp_file.name) as zipfile:
        with ZipFile(zipfile.name, 'r') as zObject:
            zObject.extractall(zipfile.name+"_raw")
        return(zipfile.name+"_raw")


def downloader_1(temp_dir):
    full_txt = ""
    for root, dirs, files in os.walk(temp_dir+"/Pages/", topdown=False):
        for name in sorted(files):
            file = os.path.join(root, name)
            if (".txt" in file) and (not ".lst" in file ):
                with open(file, "r") as f:
                    last_line = ""
                    page_txt = ""
                    lines = f.readlines()
                    first_line =  True
                    inhf = False
                    for line in lines:
                        page_txt = page_txt + last_line + "\n"
                        if ("INNEHÅLL" in line) or ("table" in line) :
                            inhf = True
                        line = re.sub(CLEANR, "", line)
                        line = re.sub("-- ", "", line)
                        line = re.sub("»", "", line)
                        if first_line:
                            first_line = False
                        else:
                            last_line = line.strip()
                    if not inhf:
                        full_txt = full_txt + page_txt
    return full_txt


def downloader_2(temp_dir):
    full_txt = ""
    for root, dirs, files in os.walk(temp_dir, topdown=False):
        for name in sorted(files):
            file = os.path.join(root, name)
            if (".html" in file) and (not "index." in file ):
                with open(file, "r") as f:
                    page_txt = ""
                    lines = f.readlines()
                    for line in lines:
                        line = re.sub(CLEANR, "", line)
                        line = re.sub("-- ", "", line)
                        line = re.sub("»", "", line)
                        page_txt = page_txt + line.strip()+"\n"
                    full_txt = full_txt + page_txt
    return full_txt



def save_file(filename,txt):
    with open(filename, "w") as f:
        f.write(txt)
        f.close()

def cleanup(temp_dir):
    if ("tmp/" in temp_dir):
        shutil.rmtree( temp_dir )
    os.remove(re.sub("_raw","",temp_dir))

input_file = os.path.join(os.path.dirname(__file__), 'runeberg_selmalagerlof_books.json')

with open(input_file) as json_file:
    books = json.load(json_file)
    
    for book in books:
        wr_file = Path("./"+book["name"]+".txt")
        if not wr_file.is_file():
            print("Downloading "+book["name"]+".txt")
            temp_dir = zipdownloader(book["url"])
            fmt = book["fmt"]
            full_txt = ""
            # let's not do switch , to be compatible with older versions 
            if fmt == 1:
                    full_txt = downloader_1(temp_dir)
            elif fmt == 2:
                    full_txt = downloader_2(temp_dir)
            save_file(wr_file,full_txt)
            cleanup(temp_dir)
    
