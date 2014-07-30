from django.db import models

class Subscriber(models.Model):
	"""Subscriber model with basic info for a user. 
	Initial creation of the model was to use first and last name, 
	but the customer decided to only use email address.
	"""
	
	first_name=models.CharField(max_length=120, null=True, blank=True)
	last_name=models.CharField(max_length=120, null=True, blank=True)
	email=models.EmailField()

	def __unicode__(self):
		return u'{0}'.format(self.email)