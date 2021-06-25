from django.test import TestCase
from authentication.models import User
from todo.models import Todo
from utils.setup_test import TestSetup






class TestMOdels(TestSetup):

    def test_should_create_todo(self):
        user= self.create_test_user()
        todo=Todo(owner=user, title="Buy mink", description='get it done')
        todo.save()

        self.assertEqual(str(todo), 'Buy mink')