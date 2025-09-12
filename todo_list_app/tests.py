from django.test import TestCase, Client 
from django.urls import reverse
from .models import Task

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