from user_api.application.user.infrastructure.address_repository import AddressRepository
from user_api.application.user.infrastructure.user_repository import UserRepository


class CreateUser:

    def __init__(self):
        self.__user_repository = UserRepository()
        self.__address_repository = AddressRepository()

    def __call__(self, name: str, birth_date: str, email: str, address: dict) -> dict:
        user = {"name": name, "birth_date": birth_date, "email": email}

        created_user = self.__user_repository.create(user=user, address=address)

        return created_user
