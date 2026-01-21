from django.contrib import messages
from django.shortcuts import redirect, render
from post_office import mail

from .forms import TestEmailForm


def send_test_email(request):
    if request.method == "POST":
        form = TestEmailForm(request.POST)
        if form.is_valid():
            mail.send(
                recipients=[form.cleaned_data["to_email"]],
                subject=form.cleaned_data["subject"],
                message=form.cleaned_data["body"],
                backend="ses",
                priority="now",
            )
            messages.success(request, "Queued test email to SES via Post Office.")
            return redirect("send-test-email")
    else:
        form = TestEmailForm()

    return render(request, "mailer/send_test_email.html", {"form": form})
