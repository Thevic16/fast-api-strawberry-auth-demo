from datetime import timedelta, datetime
import jwt
from jwt import ExpiredSignatureError, InvalidSignatureError

# app imports
from configuration.enviroment_variables import SECRET_KEY, ALGORITHM
from security.authentication import get_index_user_by_username


def create_access_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_current_user(token: str) -> bool:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise Exception("Token error: Username don't exist in payload")
    except ExpiredSignatureError:
        raise Exception("Token error: Expired signature error")
    except InvalidSignatureError:
        raise Exception("Token error: Invalid signature error")
    user_index = get_index_user_by_username(username)
    if user_index == -1:
        raise Exception("Token error: User don't exist on dataset")
    return True
