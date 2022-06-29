from datetime import timedelta, datetime
import jwt
from jwt import ExpiredSignatureError, InvalidSignatureError

# app imports
from configuration.enviroment_variables import SECRET_KEY, ALGORITHM
from data.dataset import users
from security.authentication import get_index_user_by_username


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str):
    credentials_exception = Exception("Token: Could not validate credentials")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except ExpiredSignatureError:
        raise credentials_exception
    except InvalidSignatureError:
        raise credentials_exception
    user_index = get_index_user_by_username(username)
    if user_index == -1:
        raise credentials_exception
    return users[user_index]
