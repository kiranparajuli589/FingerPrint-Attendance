from django.contrib import admin
from .models import Attendance


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_ad', 'date_bs', 'check_in', 'o_break', 'check_out', 'status')
    search_fields = ('user__email', 'user__full_name', 'date_ad')
    list_filter = ('user__full_name', 'date_ad')
    date_hierarchy = 'date_ad'
    ordering = ('-date_ad', 'user')


admin.site.register(Attendance, AttendanceAdmin)