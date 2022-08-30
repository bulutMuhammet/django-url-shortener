from django.contrib import admin
from api.models import ShortURL


@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    list_display = ["original_url", "short_url", "visit_count", "created_date"]

    class Meta:
        model = ShortURL
