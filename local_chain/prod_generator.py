import os
import subprocess
import json

accounts = []
port1 = 9011
port2 = 8100
for i in range(3):
    for j in range(5):
        for k in range(5):
            for m in range(5):
                test = subprocess.Popen(["/root/eosio/2.1/bin/cleos", "create", "key", "--to-console"], stdout=subprocess.PIPE)
                out = test.communicate()[0]
                outt = out.decode().split("\n")
                prodname = "prod"+str(i+1)+""+str(j+1)+""+str(k+1)+""+str(m+1)
                public = outt[1].split(" ")[2]
                private = outt[0].split(" ")[2]
                accounts.append({"NAME": f"{prodname}","PUBLIC_KEY": f"{public}","PRIVATE_KEY": f"{private}","PEER_ADDRESS": f"0.0.0.0:{port1}","HTTP_ADDRESS": f"0.0.0.0:{port2}","HOST_ADDRESS": f"0.0.0.0:{port1}"})
                port1 += 1
                port2 += 2

with open("accounts.json", "w+") as file:
    json.dump(accounts, file, indent = 6)