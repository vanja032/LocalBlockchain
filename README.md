# Local Blockchain Network
Package for running a local blockchain network

#### SSL Certificate setup
https://certbot.eff.org/instructions?ws=webproduct&os=ubuntufocal
```
--https-server-address 0.0.0.0:443 \
--https-certificate="<path to the ssl certificate>/fullchain.pem" \
--https-private-key="<path to the ssl key>/privkey.pem" \
```
#### Test network speed
```curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python3 -```
