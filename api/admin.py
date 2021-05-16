from django.contrib import admin

from .models import Follow

# Register your models here.

@admin.register(Follow)
class PostAdmin(admin.ModelAdmin):
    list_display = ('following', 'user')
