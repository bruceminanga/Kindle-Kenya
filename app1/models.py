from django.db import models


# Email models
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class Donation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(blank=True)
    stripe_payment_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Donation of ${self.amount} from {self.name}"


class Partnership(models.Model):
    PARTNERSHIP_CHOICES = [
        ("financial", "Financial Support"),
        ("resources", "Resource Sharing"),
        ("mentorship", "Mentorship Program"),
        ("other", "Other"),
    ]

    company_name = models.CharField(max_length=200)
    industry = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    website = models.URLField(blank=True, null=True)
    partnership_type = models.CharField(max_length=20, choices=PARTNERSHIP_CHOICES)
    description = models.TextField()
    goals = models.TextField()
    terms_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} - {self.partnership_type}"
