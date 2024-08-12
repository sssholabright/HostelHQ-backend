from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from firebase_admin import auth
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import UserProfile, AgentListing, Image, TourRequests
from .serializers import UserProfileSerializer, AgentListingSerializer, ImageSerializer, TourRequestsSerializer

@api_view(['POST'])
@csrf_exempt
def create_or_update_profile(request):
    try:
        data = request.data
        token = data.get('token')

        if not token:
            return Response({'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Verify the token
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token['uid']
        email = decoded_token.get('email', '')

        # Check if the user profile exists
        user_profile, created = UserProfile.objects.update_or_create(
            uid=uid,
            defaults={'email': email, 'name': data.get('name', ''), 'phone': data.get('phone', '')}
        )

        # Serialize the user profile
        serializer = UserProfileSerializer(user_profile)

        if created:
            return Response({'message': 'Profile created', 'profile': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Profile updated', 'profile': serializer.data}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def authenticate_user(request):
    try:
        data = request.data
        token = data.get('token')

        if not token:
            return Response({'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Verify the token
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token['uid']
        email = decoded_token.get('email', '')

        return Response({'message': 'User authenticated', 'uid': uid, 'email': email}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class AgentListingCreateView(generics.CreateAPIView):
    serializer_class = AgentListingSerializer
    parser_classes = (MultiPartParser, FormParser)
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        token = self.request.data.get('token')
        if not token:
            raise serializers.ValidationError({'error': 'Token is required'})

        try:
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']
            user_profile = UserProfile.objects.get(uid=uid)
            agent_listing = serializer.save(agent=user_profile)

            # Handle images if provided
            images_data = self.request.FILES.getlist('images')
            for image_file in images_data:
                image = Image.objects.create(image=image_file)
                agent_listing.images.add(image)

        except UserProfile.DoesNotExist:
            raise serializers.ValidationError({'error': 'User profile not found'})
        except Exception as e:
            raise serializers.ValidationError({'error': str(e)})

class AgentListingListView(generics.ListAPIView):
    queryset = AgentListing.objects.all()
    serializer_class = AgentListingSerializer
    


class AgentListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AgentListing.objects.all()
    serializer_class = AgentListingSerializer
    #permission_classes = [IsAuthenticated]

class ImageUploadView(generics.CreateAPIView):
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    # No permission_classes needed

    def post(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')

        if not images:
            return Response({'error': 'No images provided'}, status=status.HTTP_400_BAD_REQUEST)

        # Process each image
        image_objects = []
        for image_file in images:
            image = Image.objects.create(image=image_file)
            image_objects.append(image)

        serializer = ImageSerializer(image_objects, many=True)
        return Response({'message': 'Images uploaded successfully', 'images': serializer.data}, status=status.HTTP_201_CREATED)
    

from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import TourRequests, UserProfile
from .serializers import TourRequestsSerializer
import firebase_admin
from firebase_admin import auth

class TourRequestCreateView(generics.CreateAPIView):
    serializer_class = TourRequestsSerializer
    #permission_classes = [IsAuthenticated]  # Ensure user is authenticated

    def post(self, request, *args, **kwargs):
        try:
            # Get the token from request data
            token = request.data.get('token')
            if not token:
                return Response({'error': 'Token is required'}, status=status.HTTP_400_BAD_REQUEST)

            # Verify the token
            decoded_token = auth.verify_id_token(token)
            uid = decoded_token['uid']

            # Get or create UserProfile instance
            user_profile, created = UserProfile.objects.get_or_create(uid=uid)

            # Add the user profile to the request data
            request.data._mutable = True
            request.data['client'] = user_profile.id
            request.data._mutable = False

            return super().post(request, *args, **kwargs)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        

class TourRequestListView(generics.ListAPIView):
    serializer_class = TourRequestsSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return TourRequests.objects.filter(client=user)
class TourRequestUpdateView(generics.UpdateAPIView):
    serializer_class = TourRequestsSerializer
    #permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return TourRequests.objects.filter(client=user)