from random import randint

from django.test import TestCase
from faker import Faker

from .application.user.use_cases.create_user import CreateUser
from .application.user.use_cases.delete_user import DeleteUser
from .application.user.use_cases.find_users import FindUsers
from .application.user.use_cases.get_user import GetUser
from .application.user.use_cases.update_user import UpdateUser


class TestUserUseCases(TestCase):
    _faker: Faker = None

    def setUp(self):
        self._fake: Faker = Faker()

    def _generate_user(self, name: str = None, email: str = None, birth_date: str = None):
        user = {}

        if name is None:
            user['name'] = f'{self._fake.first_name()} {self._fake.last_name()}'
        if email is None:
            user['email'] = self._fake.ascii_safe_email()
        if birth_date is None:
            user['birth_date'] = self._fake.date_of_birth()

        user['address'] = {
            'street': self._fake.street_address(),
            'state': self._fake.current_country(),
            'city': self._fake.city(),
            'country': self._fake.country(),
            'zip': self._fake.postcode()
        }

        return user

    def test_get_all_users(self):

        num_users = randint(5, 30)

        for x in range(num_users):
            (CreateUser())(**self._generate_user())

        users = (FindUsers())()

        self.assertTrue(len(users) == num_users)

    def test_get_single_user(self):

        created_user = (CreateUser())(**self._generate_user())
        user = (GetUser())(user_id=created_user.id)
        self.assertTrue(
            user.id == created_user.id and \
            user.name == created_user.name and \
            user.email == created_user.email and \
            user.birth_date == created_user.birth_date
        )

    def test_delete_user(self):

        created_user = (CreateUser())(**self._generate_user())

        (DeleteUser())(user_id=created_user.id)

        user = (GetUser())(user_id=created_user.id)

        self.assertTrue(user is None)

    def test_update_user(self):

        new_name = self._fake.name()

        created_user = (CreateUser())(**self._generate_user())

        (UpdateUser())(update_user={'name': new_name}, user_id=created_user.id)

        updated_user = (GetUser())(user_id=created_user.id)

        self.assertTrue(created_user.id == updated_user.id and updated_user.name == new_name)
