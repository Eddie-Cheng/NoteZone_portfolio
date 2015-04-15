from django.contrib import admin
from registration.models import Register

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'first_name', 'last_name', 'website')
    list_filter = ('username',)
    search_fields = ('username',)
    fields = ('first_name', 'last_name', 'website')
    

admin.site.register(Register, RegisterAdmin)
