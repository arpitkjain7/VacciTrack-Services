from client.auth.api_auth import signJWT, decodeJWT


def generate_token(username: str, password: str):
    return signJWT(username=username)


def validate_token(token: str):
    return decodeJWT(token=token)
