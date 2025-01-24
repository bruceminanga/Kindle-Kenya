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


# donation feature

from django import forms
from .models import Donation, Partnership


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ["amount", "name", "email", "message"]
        widgets = {
            "amount": forms.NumberInput(attrs={"min": "1", "step": "0.01"}),
        }


class PartnershipForm(forms.ModelForm):
    class Meta:
        model = Partnership
        fields = [
            "company_name",
            "industry",
            "contact_person",
            "position",
            "email",
            "phone",
            "website",
            "partnership_type",
            "description",
            "goals",
            "terms_accepted",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
            "goals": forms.Textarea(attrs={"rows": 4}),
        }
