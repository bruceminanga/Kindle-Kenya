from django.shortcuts import render

# Email
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import NewsletterSubscriber
from .forms import NewsletterForm


# home page view.
def home(request):
    return render(request, "index.html")


# about us page views
def aboutus(request):
    return render(request, "aboutus.html")


# Email page view
class NewsletterSubscribeView(CreateView):
    model = NewsletterSubscriber
    form_class = NewsletterForm
    template_name = "base.html"
    success_url = reverse_lazy("app1:home")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Successfully subscribed to our newsletter!")
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, "This email is already subscribed or invalid.")
        return response
