from django.contrib import admin
from post_office.models import Email, EmailTemplate, Log

admin.site.register(Email)
admin.site.register(EmailTemplate)
admin.site.register(Log)
