#!/usr/bin/python

import os, pickle
from getpass import getpass
from store_safely import password_encrypt

info = {
    "user": input("User:"),
    "pass": getpass("Password: "),
    "secret": input("Secret: "),
}


if not os.path.exists("config"):
    os.makedirs("config")

with open("config/info.cfg", "wb") as f:
    f.write(password_encrypt(pickle.dumps(info), getpass("Config pass:")))
