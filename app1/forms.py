# forms.py
from django import forms
from .models import NewsletterSubscriber


class NewsletterForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your email",
                "aria-label": "Your email",
            }
        )
    )

    class Meta:
        model = NewsletterSubscriber
        fields = ["email"]
