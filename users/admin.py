""" User admin classes."""

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
 

#Models
from users.models import Profile
from django.contrib.auth.models import User



# Register your models here.

# admin.site.register(Profile)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ The profile heritage from Admin """
    list_display = ('id', 'user', 'phone_number', 'website', 'picture', 'biography')
    list_display_links = ('id', 'user')
    list_editable = ('website', 'phone_number')
    search_fields = ['user__email', 'user__username', 'user__first_name', 'user__last_name', 'website']

    list_filter = ['user__is_active', 'created', 'modified', 'user__is_staff']

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
            )
        }),
        ('Extra Info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
             ),
        }),
    )

    readonly_fields = ('created', 'modified')


class ProfileInline(admin.StackedInline):
    """ Profile in-line admin for user"""

    model = Profile
    can_delete = False
    vercose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """ Adds profile admin to base user admin"""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

