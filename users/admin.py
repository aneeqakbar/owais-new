from django.contrib import admin
from django.utils.safestring import mark_safe

from users.models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "get_image"]
    
    def get_image(self, ins):
        return mark_safe("""
                <img src="{url}" width="50px" height="50px" />
        """.format(url=ins.image.url))
    get_image.short_description = "Profile Pic"

admin.site.register(Profile, ProfileAdmin)