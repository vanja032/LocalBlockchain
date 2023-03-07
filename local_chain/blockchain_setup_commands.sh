cline create wallet --file def.txt
Key=PW5JLjYb3Pim4s8exJy1kTxgYs7kSUchj2YmjS4qYNmRgngVq5rHb

./genesis_start.sh 

python3 generate.py 

curl --request POST \
    --url http://127.0.0.1:8888/v1/producer/schedule_protocol_feature_activations \
    -d '{"protocol_features_to_activate": ["0ec7e080177b2c02b278d5088611686b49d739925a92d9bfcacd7fc6b74053bd"]}'

cline set contract inery ./inery.boot/

./activate_features.sh 

cline set contract inery ./inery.system inery.system.wasm inery.system.abi

cline set contract inery.token ./inery.token inery.token.wasm inery.token.abi

cline push action inery.token create '[ "inery", "800000000.0000 INR" ]' -p inery.token@active

cline push action inery.token issue '[ "inery", "450000000.0000 INR", "Issuing tokens for inery account" ]' -p inery@active

cline push action inery init '["0", "4,INR"]' -p inery@active
