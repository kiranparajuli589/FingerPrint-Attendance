from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


class MyUserAdmin(UserAdmin):
    list_display = ('full_name', 'email', 'fingercode', 'date_created', 'is_admin', 'is_staff', 'is_active')
    list_filter = ('is_admin', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('fingercode', 'full_name')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'fingercode', 'password1', 'password2')}
         ),
    )

    search_fields = ('email', 'full_name')
    date_hierarchy = 'date_created'
    ordering = ('full_name','date_created')

    filter_horizontal = ()


class ProfileAdmin(UserAdmin):
    list_display = ('user', 'address', 'group', 'phone')
    list_filter = ('is_admin', 'is_staff')

    search_fields = ('user__email', 'user__full_name')
    list_filter = ('user__full_name', 'group')
    ordering = ('user',)
    filter_horizontal = ()


admin.site.register(User, MyUserAdmin)
admin.site.register(Profile, ProfileAdmin)
