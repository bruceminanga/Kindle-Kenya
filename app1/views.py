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


# donation feature

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DonationForm, PartnershipForm
from decimal import Decimal
import stripe  # You'll need to pip install stripe

stripe.api_key = "your_stripe_secret_key"  # Store this in environment variables


def donation_view(request):
    form = DonationForm()
    return render(request, "donations/donate.html", {"form": form})


def process_donation(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            try:
                # Create Stripe payment intent
                amount = int(
                    float(form.cleaned_data["amount"]) * 100
                )  # Convert to cents
                payment_intent = stripe.PaymentIntent.create(
                    amount=amount,
                    currency="usd",
                    description=f"Donation from {form.cleaned_data['email']}",
                )

                # Save donation to database
                donation = form.save(commit=False)
                donation.stripe_payment_id = payment_intent.id
                donation.save()

                return redirect("donation_success")
            except Exception as e:
                messages.error(request, "Payment processing failed. Please try again.")
                return redirect("donation")
    return redirect("donation")


# views.py
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import PartnershipForm
import json
import logging

logger = logging.getLogger(__name__)


@ensure_csrf_cookie
@require_http_methods(["POST"])
def submit_partnership(request):
    logger.info("Partnership submission view called")

    try:
        # Log the raw request body
        logger.info(f"Raw request body: {request.body.decode()}")

        # Parse the JSON data
        data = json.loads(request.body)
        logger.info(f"Parsed form data: {data}")

        # Create form instance
        form = PartnershipForm(data)
        logger.info(f"Form created with data")

        # Check form validity
        if form.is_valid():
            logger.info("Form is valid")
            # Save the form and get the instance
            partnership = form.save()
            logger.info(f"Partnership saved with ID: {partnership.id}")

            # Log the saved data
            logger.info(f"Saved partnership data: {partnership.__dict__}")

            return JsonResponse(
                {
                    "status": "success",
                    "message": f"Partnership application submitted successfully! ID: {partnership.id}",
                }
            )
        else:
            logger.error(f"Form validation errors: {form.errors}")
            return JsonResponse({"status": "error", "errors": form.errors}, status=400)

    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {str(e)}")
        return JsonResponse(
            {"status": "error", "message": "Invalid JSON data"}, status=400
        )
    except Exception as e:
        logger.exception("Unexpected error in submit_partnership view")
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
