from django.test import TestCase, Client , override_settings
from django.urls import reverse
from .models import Task
import os 

# Paramètres pour la DB PostgreSQL
POSTGRES_TEST_DB = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'todo_db'),
        'USER': os.environ.get('DB_USER', 'todo_user'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'secretpassword'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

@override_settings(DATABASES=POSTGRES_TEST_DB)

class TaskModelTest(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(title="Test Task", priority="high")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.priority, "high")
        self.assertFalse(task.is_completed)

class TaskViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        
    def test_create_task(self):
        response = self.client.post(reverse('task_list'), {
            'title': 'New Task',
            'priority': 'medium'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='New Task').exists())