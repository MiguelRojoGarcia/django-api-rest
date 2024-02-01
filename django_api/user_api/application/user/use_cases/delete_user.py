from user_api.application.user.infrastructure.user_repository import UserRepository


class DeleteUser:

    def __init__(self):
        self.__user_repository = UserRepository()

    def __call__(self, user_id: int) -> None:
        return self.__user_repository.delete(user_id=user_id)
