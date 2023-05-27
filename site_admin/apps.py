from django.apps import AppConfig
from django import forms


class SiteAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_admin'

class subscribe(forms.Form):
    Email=forms.EmailField()
    def __str__(self):
        return self.Email