from django.contrib import admin
from django.contrib.auth.models import Group, User

from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken


class UserAdmin(admin.ModelAdmin):
    exclude = ['password', 'groups']

    def has_add_permission(self, request):
        return False


class OAuthApp(SocialApp):
    class Meta:
        proxy = True
        auto_created = True
        app_label = User._meta.app_label
        verbose_name = 'OAuth app'

    def __str__(self):
        return '%s (%s)' % (self.name, self.provider)


admin.site.unregister([
    EmailAddress, SocialAccount,
    SocialToken, SocialApp, User, Group
])
admin.site.register(User, UserAdmin)
admin.site.register(OAuthApp)
