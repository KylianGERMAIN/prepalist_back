import bcrypt


class Crypt_password:
    def __init__(self, password):
        self.__password = password

    def encrypt(self):
        password = self.__password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt(15))
        return hashed_password.decode('ascii')

    def compare(self, hashed_password):
        password = self.__password.encode('utf-8')
        if bcrypt.checkpw(password, hashed_password):
            print("login success")
        else:
            print("incorrect password")
