import os
import uuid
import requests

from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (AuthenticationBackend,
                                          BearerTransport, JWTStrategy)
# from google.auth.transport import requests
from google.oauth2 import id_token
from googleapiclient.discovery import build
from httplib2 import Credentials

from app.models.user import User, get_user_manager

load_dotenv()

# import env variables
SECRET = os.getenv("SECRET")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_OAUTH_CLIENT_ID")

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/google/callback")

class OAuth2Authentication:
    async def get_user(self, token: str):
        try:
            url = "https://www.googleapis.com/oauth2/v2/userinfo"
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                user_info = response.json()
                return user_info
            else:
                print(f"An error occurred: {response.json()}")
                return None
        except ValueError as error:
            print(f"An error occurred: {error}")
            return None


oauth2_authentication = OAuth2Authentication()