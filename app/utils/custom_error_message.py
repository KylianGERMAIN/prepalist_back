from enum import Enum


class Custom_Error_Message(Enum):

    # Username
    USERNAME_LENGTH = "Your username length must be at least 5 characters"

    # Email
    INVALID_EMAIL_ADRESS = "Your email is not valid"
    EMAIL_ALREADY_EXIST = "The email already exist",

    # Password
    PASSWORD_LENGTH = "Your password length must be at least 7 characters",
    BAD_PASSWORD = "The password is incorrect",

    # Authorization
    NO_AUTHORIZATION = "No authorization",
    INVALID_TOKEN = "Your authorization bearer token is not valid",

    # Authentification
    ADD_USER = 'Error during insertion of the data in the database'
