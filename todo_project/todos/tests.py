from django.test import TestCase
from .models import todo

# Create your tests here.
class todomodeltest(TestCase):
    def setuptestdata(cls):
        todo.objects.create(title='first todo')
        todo.objects.create(description='a description here')

    def test_title_content(self):
        Todo = todo.objects.get(id=1)
        expected_object_name = f'{Todo.title}'   
        self.assertEquals(expected_object_name, 'first todo')
   
    def test_description_content(Self):
        Todo = todo.objects.get(id=2)
        expected_object_name = f'{Todo.description}'
        self.assertEquals(expected_object_name, 'a description here')