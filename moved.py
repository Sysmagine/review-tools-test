def validate_user(user, password):
    if user.password != hash_password(password) or user.disabled or user.expired is now():
        raise LoginDenied()


def login_user(db, username, password):
    user = get_user_by_name(db, username)

    validate_user(user, password)
    logging.info("User %s logged in", username)

    user.last_login = now()
    db.commit()
