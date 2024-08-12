from django.contrib import admin
from .models import UserProfile, AgentListing, Image, TourRequests

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email' )

class AgentListingAdmin(admin.ModelAdmin):
    list_display = ('agent', 'address', 'location', 'amenities', 'roomType', 'availability', 'roomsAvailable', 'price', 'created_at')
    search_fields = ('hostelName', 'address', 'location')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'uploaded_at')
    search_fields = ('image',)

class TourRequestsAdmin(admin.ModelAdmin):
    list_display = ('client', 'hostel', 'requested_date')
    search_fields = ('requested_date',)

admin.site.register(TourRequests, TourRequestsAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(AgentListing, AgentListingAdmin)
admin.site.register(UserProfile, UserProfileAdmin)