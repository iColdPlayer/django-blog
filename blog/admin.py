from django.contrib import admin
from blog.models import Post
from django.db import models
from martor.widgets import AdminMartorWidget


admin.site.site_header = "Welcome To iColdPlayer"
admin.site.site_title = "iColdPlayer Administrator"
admin.site.site_index = "iColdPlayer"


class Blog(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


admin.site.register(Post)