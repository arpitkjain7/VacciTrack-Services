import time
from typing import Dict

import jwt
from decouple import config


JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def token_response(token: str):
    return {"access_token": token}


def signJWT(username: str):
    payload = {"username": username, "expires": time.time() + 600}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decodeJWT(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}


if __name__ == "__main__":
    # token = signJWT("arpit")
    # print(token)
    # print(time.time())
    # print(time.time() + 600)
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYXJwaXQiLCJleHBpcmVzIjoxNjI1MDcxODA3Ljg4ODI3MDF9.7Tq-kv6MMR_q9kaI7ZVSfvf1u1CQlHtpxEPS1DIz824"
    decoded = decodeJWT(token)
    print(decoded)
    # import os
    # import binascii

    # print(binascii.hexlify(os.urandom(24)))
