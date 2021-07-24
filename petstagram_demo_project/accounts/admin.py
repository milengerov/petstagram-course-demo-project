from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext, gettext_lazy as _

from django.contrib.auth.admin import UserAdmin

from petstagram_demo_project.accounts.models import PetstagramUser

UserModel = get_user_model()


# @admin.register(PetstagramUser)
# instead of the above use the func get_user_model() that gives us the UserModel from
# AUTH_USER_MODEL from the settings
@admin.register(UserModel)
class PetstagramUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # (_('Personal info'), {'fields': []}),
        (_('Permissions'), {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', ),
        }),
    )

    readonly_fields = ('date_joined',)

    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('email',)
    ordering = ('email',)

# admin.site.register(PetstagramUser.PetstagramUserAdmin)