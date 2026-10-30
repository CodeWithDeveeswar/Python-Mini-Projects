# Duplicate File Finder

import os, hashlib

folder = input("Folder path: ")
hashes = {}

for filename in os.listdir(folder):
    path = f"{folder}/{filename}"
    fille_hash = hashlib.md5(open(path, "rb")\
                             .read()).hexdigest()

    if fille_hash in hashes:
        print(f"Duplicate: \
              \n {filename} = {hashes[fille_hash]}")
    else:
        hashes[fille_hash] = filename