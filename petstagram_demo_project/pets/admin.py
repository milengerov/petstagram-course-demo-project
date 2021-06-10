from django.contrib import admin

# Register your models here.

from petstagram_demo_project.pets.models import Pet, Like

class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "age", "likes_count")

    def likes_count(self, current_object):
        return current_object.like_set.count()



admin.site.register(Pet, PetAdmin)
admin.site.register(Like)
