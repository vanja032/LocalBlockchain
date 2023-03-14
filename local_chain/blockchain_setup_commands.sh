cleos create wallet --file def.txt
Key=<wallet default unlock key>

cleos wallet unlock --password <wallet default unlock key>

cleos wallet import --private-key <private development key>

./genesis_start.sh 

python3 generate.py 

curl --request POST \
    --url http://127.0.0.1:8888/v1/producer/schedule_protocol_feature_activations \
    -d '{"protocol_features_to_activate": ["0ec7e080177b2c02b278d5088611686b49d739925a92d9bfcacd7fc6b74053bd"]}'

cleos set contract eosio ./eosio/build/contracts/contracts/eosio.boot/

./activate_features.sh 

cleos set contract eosio ./eosio.system eosio.system.wasm eosio.system.abi

cleos set contract eosio.token ./eosio.token eosio.token.wasm eosio.token.abi

cleos push action eosio.token create '[ "eosio", "800000000.0000 EOS" ]' -p eosio.token@active

cleos push action eosio.token issue '[ "eosio", "450000000.0000 EOS", "Issuing tokens for eosio account" ]' -p eosio@active

cleos push action eosio init '["0", "4,EOS"]' -p eosio@active
