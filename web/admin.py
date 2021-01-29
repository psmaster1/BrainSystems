from django.contrib import admin
from .models import Contact, PageSettings, FAQs


class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']
    list_display = ['first_name', 'last_name', 'phone_number', 'email', 'country', 'house_type', 'living_space',
                    'message']


admin.site.register(FAQs)
admin.site.register(Contact, ContactAdmin)
admin.site.register(PageSettings)

