from django.contrib import admin
from django.urls import include, path
from django_ses.views import SESEventWebhookView

urlpatterns = [
    path('ses/event-webhook/', SESEventWebhookView.as_view(), name='event_webhook'),
    path('admin/django-ses/', include('django_ses.urls')),
    path('admin/', admin.site.urls),
    path("", include("mailer.urls")),
]
