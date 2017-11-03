from project import db
from project.api.models import User
from project.tests.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def test_add_user(self):
        user = User(
            username='justatest',
            email='test@test.com',
        )
        db.session.add(user)
        db.session.commit()
        self.assertTrue(user.id)
        self.assertEqual(user.username, 'justatest')
        self.assertEqual(user.email, 'test@test.com')
        self.assertTrue(user.active)
        self.assertTrue(user.created_at)