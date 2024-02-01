from user_api.application.user.infrastructure.user_repository import UserRepository


class FindUsers:

    def __init__(self):
        self.__user_repository = UserRepository()

    def __call__(self) -> list:
        return self.__user_repository.find()
