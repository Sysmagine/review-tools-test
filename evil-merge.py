def login_user(db, username, password):
    user = get_user_by_name(db, username)

    if user.password != hash_password(password) or user.disabled:
        raise LoginDenied()

    user.last_login = now()
    db.commit()
