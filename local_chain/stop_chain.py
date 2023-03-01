#!/usr/bin/python3
import subprocess
import time
import json
import os

max_accounts = 25
num = 1

with open("accounts.json", "r+") as file:
    accounts = json.loads(file.read())
    os.chdir("local")
    for account in accounts:
        try:
            os.chdir("local_" + account["NAME"])
            process_pid = subprocess.Popen(["cat", "blockchain/eosd.pid"], stdout=subprocess.PIPE).communicate()[0].decode()
            os.system(f"kill -2 {process_pid}")
            print(f"Killed process pid={process_pid}")
            os.chdir("..")
            time.sleep(1)
        except Exception as ex:
            print(ex)
            pass

        if num >= max_accounts:
            break
        num += 1
    
    os.system("rm -rf *")