# Simple Contact Book

import json

try:
    with open("contacts.json", "r") as f:
        contacts = json.load(f)
except FileNotFoundError:
    contacts = {}

choice = input("1.Add 2.View: ")

if choice == "1":
    name = input("Name: ")
    contacts[name] = input("Phone: ")
    with open ("contacts.json", "w") as f:
        json.dump(contacts, f)
else:
    for name, phone in contacts.items():
        print(f"{name}: {phone}")