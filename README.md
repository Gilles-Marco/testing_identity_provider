## Start

```bash
docker compose up
```

username and password are in the .env file

The content of keykloak/realm-exports.json will be automatically imported

## Openid configuration

http://localhost:8080/realms/my-it/.well-known/openid-configuration

## JWKS Keys

http://localhost:8080/realms/my-it/protocol/openid-connect/certs

## Open ID token

http://localhost:8080/realms/my-it/protocol/openid-connect/tokens

## Create a client

Create a client with the option "Client Authentication" and "Service account roles" 

Download client secret to generate an id token later

## Configure default algorithm signature

Go to Realm => Tokens
And mofidy the "Default Signature Algorithm" by ES384

## Run test

```bash
cd idp
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
python get_token_id.py
```

Before running this command you should have done the start step