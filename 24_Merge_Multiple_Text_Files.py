# Merge Multiple Text Files

import glob

with open("merged.txt", "w") as outFile:
    for filename in glob.glob("*.txt"):
        with open(filename, "r") as inFile:
            outFile.write(inFile.read() + "\n")

print("All files merged into merged.txt ✅")