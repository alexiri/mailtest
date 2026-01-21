from django import forms


class TestEmailForm(forms.Form):
    to_email = forms.EmailField(label="To")
    subject = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea, label="Message")
