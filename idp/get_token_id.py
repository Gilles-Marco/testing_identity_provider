import requests
from values import REALMS, REALMS_CLIENT
import base64
import jwt
import json

def get_id_token(client_info):
    response = requests.post(
        url=client_info["client_token_endpoint"],
        data={
            "scope": "openid",
            "grant_type": "client_credentials",
            "client_id": client_info["client_id"],
            "client_secret": client_info["client_secret"]
        }
    ).json()
    token=response["access_token"]
    return token

def get_header(token):
    return json.loads(base64.b64decode(token.split(".")[0] + "==").decode())

def get_body(token):
    return json.loads(base64.b64decode(token.split(".")[1] + "==").decode())

def verify_signature(kid, alg, token, client_info):
    RSA_ALGORITHMS = ["RS256", "RS384", "RS512", "PS256", "PS384", "PS512"]
    ECSDA_ALGORITHMS = ["ES256", "ES256K", "ES384", "ES512"]
    algClass = None
    if alg in RSA_ALGORITHMS:
        from jwt.algorithms import RSAAlgorithm
        algClass = RSAAlgorithm
    elif alg in ECSDA_ALGORITHMS:
        from jwt.algorithms import ECAlgorithm
        algClass = ECAlgorithm
    else:
        raise Exception(f"JWT Auth {alg} not implemented")
    jwks_keys = requests.get(client_info["client_jwks_endpoint"]).json()["keys"]
    sig_key = list(filter(lambda jwks_key: jwks_key["kid"] == kid, jwks_keys))[0]
    public_key = algClass.from_jwk(json.dumps(sig_key))
    return jwt.decode(
        jwt=token,
        key=public_key,
        algorithms=[alg],
        options={
            "verify_aud": False
        }
    )

def info_id_token(client_info):
    token=get_id_token(client_info)
    header=get_header(token)
    body=get_body(token)
    print(token)
    print(header)
    print(body)
    try:
        verify_signature(header["kid"], header["alg"], token, client_info)
        print("Token signature is verified")
    except Exception as error:
        print(error)

if __name__ == "__main__":
    for realm in REALMS:
        info_id_token(REALMS_CLIENT[realm])