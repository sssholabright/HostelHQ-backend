from django.contrib import admin
from .models import User, Agent, Guest

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_agent', 'is_guest')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('date_joined',)

class AgentAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('user__email', )

class GuestAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', )
    search_fields = ('user__email', 'phone_number')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Agent, AgentAdmin)
admin.site.register(Guest, GuestAdmin)
