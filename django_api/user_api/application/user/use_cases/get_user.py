from user_api.application.user.infrastructure.user_repository import UserRepository


class GetUser:

    def __init__(self):
        self.__user_repository = UserRepository()

    def __call__(self, user_id: int) -> dict | None:
        return self.__user_repository.findOne(user_id=user_id)
