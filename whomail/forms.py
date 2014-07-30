from django.forms import ModelForm
from django import forms
from whomail import models

class SubscriberForm(ModelForm):
	'''Custom Model form for placeholder text
	'''

	def __init__(self,*args, **kwargs):
		"""A more difficult way to add atts to the text input form field.
		"""

		super(SubscriberForm,self).__init__(*args, **kwargs)
		field=self.fields.get('email')

		if field:
			field.widget=forms.TextInput(
				attrs={'placeholder': 'someone@email.com'})

	class Meta:
		model=models.Subscriber
		fields=['email',]