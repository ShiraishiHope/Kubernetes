# todo_list_app/tests.py
from django.test import TestCase, Client 
from django.urls import reverse
from .models import Task

class TaskModelTest(TestCase):
    def test_task_creation(self):
        # Use the correct priority value based on your model choice
        task = Task.objects.create(title="Test Task", priority="high")  # if using Option A
        # OR: task = Task.objects.create(title="Test Task", priority="1")  # if using Option B
        
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.priority, "high")  # Adjust based on your choice
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
            'priority': 'medium'  # This should work with Option A
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title='New Task').exists())
        
        # Verify the priority was saved correctly
        task = Task.objects.get(title='New Task')
        self.assertEqual(task.priority, 'medium')  # Adjust based on your choice