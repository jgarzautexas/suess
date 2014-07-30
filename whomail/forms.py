from django.forms import ModelForm
from django import forms
from whomail.models import Subscriber

class SubscriberForm(ModelForm):
	'''Custom Model form for placeholder text
	'''

	def __init__(self,*args, **kwargs):
		super(SubscriberForm,self).__init__(*args, **kwargs)
		field=self.fields.get('email')
		if field:
			field.widget=forms.TextInput(
				attrs={'placeholder': 'someone@email.com'})
	class Meta:
		model=Subscriber
		fields=['email',]