from django.contrib import admin
from .models import SAIDRecord, PublicHoliday

class SAIDRecordAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'date_of_birth', 'gender', 'citizenship_status', 'search_count')
    search_fields = ('id_number',)
    list_filter = ('gender', 'citizenship_status')
    ordering = ('id_number',)

class PublicHolidayAdmin(admin.ModelAdmin):
    list_display = ('id_record', 'holiday_name', 'date', 'holiday_type')
    search_fields = ('holiday_name', 'holiday_type')
    list_filter = ('holiday_type', 'date')
    ordering = ('date',)

# Register the models with the admin site
admin.site.register(SAIDRecord, SAIDRecordAdmin)
admin.site.register(PublicHoliday, PublicHolidayAdmin)
