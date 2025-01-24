from django.contrib import admin

# Register your models here.

from .models import NewsletterSubscriber


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ["email", "created_at", "is_active"]


# admin.py
from django.contrib import admin
from .models import Partnership


@admin.register(Partnership)
class PartnershipAdmin(admin.ModelAdmin):
    list_display = (
        "company_name",
        "contact_person",
        "email",
        "partnership_type",
        "created_at",
    )
    list_filter = ("partnership_type", "created_at", "industry")
    search_fields = ("company_name", "contact_person", "email", "industry")
    readonly_fields = ("created_at",)
    date_hierarchy = "created_at"

    fieldsets = (
        ("Company Information", {"fields": ("company_name", "industry", "website")}),
        (
            "Contact Information",
            {"fields": ("contact_person", "position", "email", "phone")},
        ),
        (
            "Partnership Details",
            {"fields": ("partnership_type", "description", "goals")},
        ),
        ("Additional Information", {"fields": ("terms_accepted", "created_at")}),
    )

    def has_add_permission(self, request):
        # Optional: Disable adding partnerships directly from admin
        return False

    def has_delete_permission(self, request, obj=None):
        # Optional: Disable deletion of partnerships from admin
        return False
