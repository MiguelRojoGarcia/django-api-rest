from user_api.application.user.infrastructure.address_repository import AddressRepository
from user_api.application.user.infrastructure.user_repository import UserRepository


class UpdateUser:

    def __init__(self):
        self.__user_repository = UserRepository()
        self.__address_repository = AddressRepository()

    def __call__(self, update_user: dict, user_id: int) -> dict:
        if 'address' in update_user and update_user['address'] is not None:
            user = self.__user_repository.findOne(user_id)
            address = update_user['address']
            self.__address_repository.update(update_address=address, address_id=user.address_id)

        return self.__user_repository.update(user_id=user_id, update_user=update_user)
