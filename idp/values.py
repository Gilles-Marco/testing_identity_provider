IDP_PROTOCOL="http"
IDP_HOST="localhost:8080"

REALMS_CLIENT = {
    "litellm-test-es384": {
        "client_id": "litellm-test-openid-app-es384",
        "client_secret": "SLUCQGvB24gtSd9UiJWvq4G3pTCr6s1P",
        "client_token_endpoint": f"{IDP_PROTOCOL}://{IDP_HOST}/realms/litellm-test-es384/protocol/openid-connect/token",
        "client_jwks_endpoint": f"{IDP_PROTOCOL}://{IDP_HOST}/realms/litellm-test-es384/protocol/openid-connect/certs"
    },
    "litellm-test-rsa256": {
        "client_id": "litellm-test-openid-app-rsa256",
        "client_secret": "b5gXxk9GDqJqe3wzdsLzUh4WUjslgs8z",
        "client_token_endpoint": f"{IDP_PROTOCOL}://{IDP_HOST}/realms/litellm-test-rsa256/protocol/openid-connect/token",
        "client_jwks_endpoint": f"{IDP_PROTOCOL}://{IDP_HOST}/realms/litellm-test-rsa256/protocol/openid-connect/certs"
    }
}
REALMS = REALMS_CLIENT.keys()