from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from todos.models import Todo

User = get_user_model()


class TodoSsrCrudTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='u1',
            email='u1@example.com',
            password='StrongPassword!234',
        )
        self.client.login(username='u1', password='StrongPassword!234')

    def test_full_crud_path(self):
        # Create
        create_url = reverse('todos:create')
        resp = self.client.post(create_url, data={
            'title': 'First todo',
            'description': 'Desc',
            'due_date': '',
        })
        self.assertEqual(resp.status_code, 302)
        todo = Todo.objects.get(owner=self.user, title='First todo')

        # Edit
        edit_url = reverse('todos:edit', args=[todo.id])
        resp = self.client.post(edit_url, data={
            'title': 'First todo updated',
            'description': 'Desc updated',
            'due_date': '',
            'is_completed': False,
        })
        self.assertEqual(resp.status_code, 302)
        todo.refresh_from_db()
        self.assertEqual(todo.title, 'First todo updated')

        # Toggle complete
        toggle_url = reverse('todos:toggle', args=[todo.id])
        resp = self.client.post(toggle_url)
        self.assertIn(resp.status_code, (200, 302))
        todo.refresh_from_db()
        self.assertTrue(todo.is_completed)

        # Delete
        delete_url = reverse('todos:delete', args=[todo.id])
        resp = self.client.post(delete_url)
        self.assertIn(resp.status_code, (200, 302))
        self.assertFalse(Todo.objects.filter(id=todo.id).exists())
