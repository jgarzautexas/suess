from django.db import models


class Subscriber(models.Model):
	first_name=models.CharField(max_length=120, null=True, blank=True)
	last_name=models.CharField(max_length=120, null=True, blank=True)
	email=models.EmailField()

	def __unicode__(self):
		return self.email