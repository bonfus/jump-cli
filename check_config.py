#!/usr/bin/python

import os, pickle, sys
from getpass import getpass
from store_safely import password_decrypt

if not os.path.exists("config/info.cfg"):
    print("No config file, run gen_config.py")
    sys.exit(1)


with open("config/info.cfg") as f:
    config_pass = getpass("Config Password: ")
    if config_pass == "":
        print("WARNING: No config file password!")

    try:
        info = pickle.loads(password_decrypt(f.read(), config_pass))
        print("Config parsed Correctly!")
    except:
        print("Error parsing config (wrong password?)")
