from client.crud.user import create_record


def register_user(user_data: dict):
    return create_record(user_data)
