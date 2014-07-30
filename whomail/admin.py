from django.contrib import admin
from whomail import models

class SubscriberAdmin(admin.ModelAdmin):
	list_display	= ('email', "first_name", "last_name")
	list_filter 	= ("email", "last_name")
	search_fields	= ["email", "last_name"]

admin.site.register(models.Subscriber, SubscriberAdmin)