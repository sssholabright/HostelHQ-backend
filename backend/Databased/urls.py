from django.urls import path
from .views import (
    AgentListingCreateView,
    AgentListingListView,
    AgentListingDetailView,
    authenticate_user,
    create_or_update_profile,
    ImageUploadView
)

urlpatterns = [
    # User profile
    path('authenticate/', authenticate_user, name='authenticate_user'),
    path('create-or-update-profile/', create_or_update_profile, name='create_or_update_profile'),

    # Agent Listings
    path('agent-listings/', AgentListingListView.as_view(), name='agent-listing-list'),  # GET for listing
    path('agent-listings/create/', AgentListingCreateView.as_view(), name='agent-listing-create'),  # POST for creation
    path('agent-listings/<int:pk>/', AgentListingDetailView.as_view(), name='agent-listing-detail'),  # GET, PUT, DELETE for detail

    # Image uploads
    path('upload-images/', ImageUploadView.as_view(), name='upload-images'),
]
