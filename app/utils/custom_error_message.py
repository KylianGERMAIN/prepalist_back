from enum import Enum


class Custom_Error_Message(Enum):

    # User
    USER_DOES_NOT_EXIST = "The user does not exist"

    # Username
    USERNAME_LENGTH = "Your username length must be at least 5 characters"

    # Email
    INVALID_EMAIL_ADRESS = "The email is not valid"
    EMAIL_ALREADY_EXIST = "The email already exist"

    # Password
    PASSWORD_LENGTH = "Your password length must be at least 7 characters"
    BAD_PASSWORD = "The password is incorrect"

    # Authorization
    NO_AUTHORIZATION = "You are not authorized to access this resource"
    INVALID_TOKEN = "Invalid token"

    # Authentification
    ADD_USER = "Error while adding user to database"
    CHECKING_USER = 'Error while checking user in database'

    # Meal
    MEAL_ALREADY_EXIST = "The meal already exist"
    CHECKING_MEAL = "Error while checking meal in database"
    NO_INGREDIENTS = 'You must add at least one ingredient'
    REMOVE_MEAL = "Error while removing meal from database"
    MEAL_DOES_NOT_EXIST = "The meal does not exist"
    FIND_MEAL = "Error while finding meal in database"

    # Create my week
    NOT_SUNDAY = "You must create your week on sunday"
