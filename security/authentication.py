from data.dataset import users


def get_index_user_by_username(username: str) -> int:
    usernames = [user.username for user in users]
    try:
        return usernames.index(username)
    except ValueError:
        return -1


def authenticate_user(username: str, password: str) -> bool:
    user_index = get_index_user_by_username(username)

    if user_index == -1:
        return False

    user = users[user_index]
    if user.password != password:
        return False
    return True

