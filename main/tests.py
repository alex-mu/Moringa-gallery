from django.test import TestCase
from models import category, Image
# Create your tests here.

#set up method
def setUp(self):
    self.user=category('title')
    self.user=Image('description', 'alttext', 'hashtags')

#testing instance
def test_instance(self):
    self.assertTrue(isinstance(self.user))