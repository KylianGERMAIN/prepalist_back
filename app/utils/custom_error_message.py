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
    GENERATION_REFRESH_TOKEN = "Error while generating refresh token"

    # Authentification
    LOGIN_USER = "Error while login user in database"
    REGISTER_USER = "Error while register user in database"

    # Meal
    MEAL_ALREADY_EXIST = "The meal already exist"
    NO_INGREDIENTS = 'You must add at least one ingredient'
    REMOVE_MEAL = "Error while removing meal from database"
    MEAL_DOES_NOT_EXIST = "The meal does not exist"
    FIND_MEAL = "Error while finding meal in database"
    FIND_MEALS = "Error while finding meals in database"
    UPDATE_MEAL = "Error while updating meal in database"
    NO_ENOUGH_MEALS = "You must add at least 10 meals to create your week"
    MEAL_NO_NAME = "You must add a name to your meal"
    ADD_MEAL = "Error while adding meal to database"

    # Create my week
    NO_WEEK = "You must create your week"
    WEEK_NOT_GENERATED = "Error while generating week"
    NO_ENOUGH_DAYS = "Your week must contain 7 days"

    # List ingredients
    CHECKING_LIST_INGREDIENTS = "Error while checking list ingredients in database"
    NO_ENOUGH_MEAL_TO_GET_INGREDIENTS = "Your week must contain at least 1 meals to get ingredients"
