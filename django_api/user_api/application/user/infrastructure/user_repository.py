from user_api.models import Address as ModelAddress
from user_api.models import User as ModelUser


class UserRepository:

    def find(self) -> list:
        return ModelUser.objects.all()

    def findOne(self, user_id: int) -> dict | None:
        return ModelUser.objects.filter(id=user_id).first()

    def create(self, user: dict, address: dict = None) -> None:

        if address is not None:
            address = ModelAddress.objects.create(**address)

        user = ModelUser.objects.create(
            name=user['name'],
            email=user['email'],
            birth_date=user['birth_date'],
            address=address
        )

        return user

    def update(self, user_id: int, update_user: dict) -> dict:
        user = ModelUser.objects.filter(id=user_id).first()

        for field in ['name', 'email', 'birth_date']:
            if field in update_user:
                setattr(user, field, update_user[field])

        user.save()

        return user

    def delete(self, user_id: int) -> None:
        ModelUser.objects.filter(id=user_id).delete()
