import subprocess
import json
from time import sleep

# all eosio account 
# eosio
# eosio.bpay    
# eosio.msig    
# eosio.names   
# eosio.ram     
# eosio.ramfee  
# eosio.saving  
# eosio.stake   
# eosio.token   
# eosio.vpay    
# eosio.wrap    

def create_accounts():

    wallet_password = "<wallet default unlock password>"
    system_accounts = '[ \n'

    my_list = ['eosio.bpay',
            'eosio.msig',
            'eosio.names',
            'eosio.ram',
            'eosio.ramfee',
            'eosio.saving',
            'eosio.stake',
            'eosio.token',
            'eosio.vpay',
            'eosio.wrap',
            'eosio.rex',
            'eosio.reserv']

    subprocess.run(["cleos", "wallet", "unlock", "--password", f"{wallet_password}"], stdout=subprocess.PIPE)

    for el in my_list:
        key_pair    = subprocess.Popen(["cleos", "create", "key", "--to-console"], stdout=subprocess.PIPE)
        output      = key_pair.communicate()[0].decode().strip()
        private_key = output[13:64].strip()
        public_key  = output[77:].strip()

        system_accounts += '{'
        system_accounts += f'"NAME": "{el}",\n "PRIVATE_KEY": "{private_key}",\n "PUBLIC_KEY": "{public_key}"\n'
        system_accounts += '},\n'

        subprocess.run(["cleos", "create", "account", "eosio", f"{el}", f"{public_key}"], stdout=subprocess.PIPE)
        subprocess.run(["cleos", "wallet", "import", "--private-key", f"{private_key}"], stdout=subprocess.PIPE)
        sleep(2)

    system_accounts = system_accounts[0:len(system_accounts) - 2]
    system_accounts += '\n]'

    json_data = json.loads(system_accounts)
    
    with open('system_accounts.json', 'w+') as f:
        json.dump(json_data, f, indent=4)

if __name__ == '__main__':  

    create_accounts()

