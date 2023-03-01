#!/usr/bin/python3
import subprocess
import time
import json
import os

wallet_deffault = "<wallet default password>"
max_accounts = 25
num = 1

with open("accounts.json", "r+") as file:
    accounts = json.loads(file.read())
    os.chdir("local")
    subprocess.run(["cleos", "wallet", "unlock", "--password", f"{wallet_deffault}"])
    for account in accounts:
        try:
            os.makedirs("local_" + account["NAME"])
            os.chdir("local_" + account["NAME"])
            with open("start_producer.sh", "w+") as file:
                file.write(f'''
#!/bin/bash
DATADIR="./blockchain"

if [ ! -d $DATADIR ]; then
mkdir -p $DATADIR;
fi

nodeos \\
--genesis-json $DATADIR"/../genesis.json" \\
--plugin eosio::producer_plugin \\
--plugin eosio::producer_api_plugin \\
--plugin eosio::chain_plugin \\
--plugin eosio::chain_api_plugin \\
--plugin eosio::http_plugin \\
--plugin eosio::history_api_plugin \\
--plugin eosio::history_plugin \\
--plugin eosio::net_plugin \\
--plugin eosio::net_api_plugin \\
--filter-on=* \\
--data-dir $DATADIR"/data" \\
--blocks-dir $DATADIR"/blocks" \\
--config-dir $DATADIR"/config" \\
--access-control-allow-origin=* \\
--contracts-console \\
--http-validate-host=false \\
--verbose-http-errors \\
--enable-stale-production \\
--p2p-max-nodes-per-host 100 \\
--connection-cleanup-period 10 \\
--producer-name {account["NAME"]} \\
--http-server-address {account["HTTP_ADDRESS"]} \\
--p2p-listen-endpoint {account["PEER_ADDRESS"]} \\
--p2p-peer-address 0.0.0.0:9010 \\
--signature-provider {account["PUBLIC_KEY"]}=KEY:{account["PRIVATE_KEY"]} \\
>> $DATADIR"/nodeos.log" 2>&1 & \\
echo $! > $DATADIR"/eosd.pid"
''')
            genesis_json = {
                "initial_timestamp": "2023-01-05T08:55:11.000",
                "initial_key": "<initial development key>",
                "initial_configuration": {
                    "max_block_net_usage": 1048576,
                    "target_block_net_usage_pct": 1000,
                    "max_transaction_net_usage": 524288,
                    "base_per_transaction_net_usage": 12,
                    "net_usage_leeway": 500,
                    "context_free_discount_net_usage_num": 20,
                    "context_free_discount_net_usage_den": 100,
                    "max_block_cpu_usage": 100000,
                    "target_block_cpu_usage_pct": 500,
                    "max_transaction_cpu_usage": 50000,
                    "min_transaction_cpu_usage": 100,
                    "max_transaction_lifetime": 3600,
                    "deferred_trx_expiration_window": 600,
                    "max_transaction_delay": 3888000,
                    "max_inline_action_size": 4096,
                    "max_inline_action_depth": 4,
                    "max_authority_depth": 6
                },
                "initial_chain_id": "0000000000000000000000000000000000000000000000000000000000000000"
            }
            with open("genesis.json", "w+") as file:
                json.dump(genesis_json, file, indent = 6)

            os.chmod("start_producer.sh", 777)
            os.system("./start_producer.sh")
            account_name = account["NAME"]
            private_key = account["PRIVATE_KEY"]
            public_key = account["PUBLIC_KEY"]
            url = account["HOST_ADDRESS"]
            subprocess.run(["cleos", "wallet", "import", "--private-key", f"{private_key}"])
            subprocess.run(["cleos", "system", "newaccount", "eosio", "--transfer", f"{account_name}", f"{public_key}", f"{public_key}", "--stake-net=1 INR", "--stake-cpu=1 INR", "--buy-ram-bytes=1048576"])
            #subprocess.run(["cleos", "transfer", "eosio", f"{account_name}", "50000 INR"])
            print("Account created successfully")
            subprocess.run(["cleos", "system", "regproducer", f"{account_name}", f"{public_key}", f"{url}"])
            print("Account registered successfully")
            subprocess.run(["cleos", "system", "voteproducer", "approve", "eosio", f"{account_name}"])
            print("Account approved successfully")
            os.chdir("..")
            time.sleep(1)
        except Exception as ex:
            print(ex)
            # directory already exists
            pass

        if num >= max_accounts:
            break
        num += 1