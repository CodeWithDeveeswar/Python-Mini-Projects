# Bulk File Renamer

import os

folder = input("Folder path: ")
prefix = input("New name prefix: ")

for i, file_nm in enumerate(os.listdir(folder), 1):
    ext = file_nm.split(".")[-1]
    os.rename(f"{folder}/{file_nm}", \
              f"{folder}/{prefix}_{i}.{ext}")