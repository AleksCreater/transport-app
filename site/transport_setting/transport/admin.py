from django.contrib import admin
from .models import User
from .models import Rubric

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_surname', 'user_number', 'published','rubric')
    list_display_links = ('user_name', 'user_surname')
    search_fields = ('user_name', 'user_surname')
    
admin.site.register(User, UserAdmin)
admin.site.register(Rubric)

