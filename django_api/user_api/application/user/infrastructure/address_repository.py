from user_api.models import Address as ModelAddress


class AddressRepository:

    def findOne(self, address_id: int) -> dict | None:
        return ModelAddress.objects.filter(id=address_id).first()

    def create(self, address: dict) -> None:
        return ModelAddress.objects.create(**address)

    def update(self, address_id: int, update_address: dict) -> dict:
        address = ModelAddress.objects.filter(id=address_id).first()
        for field in ['street', 'state', 'city', 'country', 'zip']:
            if field in update_address:
                setattr(address, field, update_address[field])

        address.save()
        return address
