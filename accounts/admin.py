from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'first_name', 'joined')
    list_filter = ('user', 'joined')

admin.site.register(Profile, ProfileAdmin)