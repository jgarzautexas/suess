import json
from django.utils import simplejson
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from whomail import forms

def index(request):
	context={}
	if request.method=='POST':
		form=forms.SubscriberForm(request.POST)
		if form.is_valid():
			print 'i am valid'
			form.save()
			context['success'] = True
			# return HttpResponse(simplejson.dumps({'success':'Y'}))
		else:
			context['form_errors'] = form.errors

	form=forms.SubscriberForm()
	context['form']=form

	return render_to_response('index.html',
							   context,
							   context_instance=RequestContext(request)
	)