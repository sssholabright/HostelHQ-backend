from rest_framework import serializers
from .models import AgentListing, UserProfile, Image, TourRequests

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image', 'uploaded_at']

class AgentListingSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = AgentListing
        fields = "__all__"
        extra_kwargs = {
            'hostelName': {'required': False, 'allow_blank': True},
            'address': {'required': False, 'allow_blank': True},
            'description': {'required': False, 'allow_blank': True},
            'amenities': {'required': False, 'allow_blank': True},
            'availability': {'required': False, 'allow_blank': True},
            'capacity': {'required': False, 'allow_null': True},
            'price': {'required': False, 'allow_null': True},
            'owner': {'required': False},
        }

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        agent_listing = super().create(validated_data)
        
        for image_data in images_data:
            image, created = Image.objects.get_or_create(**image_data)
            agent_listing.images.add(image)
        
        return agent_listing

class TourRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourRequests
        fields = ['id', 'requested_date', 'hostel', 'client']
