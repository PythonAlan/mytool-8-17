from django.contrib import admin

# Register your models here.

from calculator.models import Rate_Info
class RateClassAdmin(admin.ModelAdmin):
    list_display = ("first_class_us",
                    "first_class_uk",
                    "first_class_de",
                    "first_class_au",
                    "second_class_us",
                    "second_class_uk",
                    "second_class_de",
                    "second_class_au",
                    "gz_us",
                    "gz_uk",
                    "gz_de",
                    "gz_au",
                    "exchange_rate_us",
                    "exchange_rate_uk",
                    "exchange_rate_de",
                    "exchange_rate_au",
                    "commission_rate",
                    )

admin.site.register(Rate_Info,RateClassAdmin)

