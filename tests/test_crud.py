import crud
from models import User, DailyLog
#username , email
user_metadata = [("mo_talab", "talab@outlook.com"), ("ceo_open_ai", "samaltman@openai.com")]
updated_usernames = ["ItsExample", "ItzSamAltman"]


users = []

def test_create_user():
    for username, email in user_metadata:
        user = crud.create_user(username,email)
        assert isinstance(user, User)
        assert user.username == username
        assert user.email == email
        users.append(user)

def test_get_user_by_email():
    for _,email in user_metadata:
        user = crud.get_user_by_email(email)
        assert isinstance(user, User)
        assert user.email == email


def test_update_username():
    for user,updated_username in zip(users,updated_usernames):
        updated_user = crud.update_username(user, updated_username)
        assert isinstance(updated_user, User)
        assert updated_user.username == updated_username






