from django.contrib import admin
from post_office.models import Email, EmailTemplate, Log

for model in (Email, EmailTemplate, Log):
	if not admin.site.is_registered(model):
		admin.site.register(model)
