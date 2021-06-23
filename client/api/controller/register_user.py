from client.crud.create_user_record import create_record


def register_user(user_data: dict):
    return create_record(user_data)
