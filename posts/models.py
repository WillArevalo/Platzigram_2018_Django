"""Posts models."""
from django.db import models

# Create your models here.
class User(models.Model):
	"""Model for User"""

	email = models.EmailField(unique=True)
	password = models.CharField(max_length=100)

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	bio = models.TextField(blank=True)

	birthdate = models.DateField(blank=True, null=True)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __init__(self, arg):
		super(User, self).__init__()
		self.arg = arg


		