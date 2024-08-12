from django.db import models

class UserProfile(models.Model):
    # Assuming this is your user profile model
    uid = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Record creation time
    
    def __str__(self):
        return self.name or self.email

class AgentListing(models.Model):
    agent = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Link to UserProfile
    uid = models.CharField(max_length=500, blank=True, null=True)
    hostelName = models.CharField(max_length=200, blank=True, null=True)  # Name of the hostel
    address = models.CharField(max_length=200, blank=True, null=True)  # Address of the hostel
    location = models.CharField(max_length=200, blank=True, null=True)  # Location of the hostel
    amenities = models.CharField(max_length=200, blank=True, null=True)  # Amenities offered
    roomType = models.CharField(max_length=200, blank=True, null=True)  # Type of room
    availability = models.CharField(max_length=20, blank=True, null=True)  # Availability status
    roomsAvailable = models.IntegerField(blank=True, null=True)  # Number of rooms available
    price = models.IntegerField(blank=True, null=True)  # Price per room
    created_at = models.DateTimeField(auto_now_add=True)  # Record creation time
    images = models.ManyToManyField('Image', blank=True)  # Link to Image model

    def __str__(self):
        return f"{self.hostelName} - {self.location}"

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.image}"

class TourRequests(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('DECLINED', 'Declined'),
    ]
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_requests')
    hostel = models.ForeignKey(AgentListing, on_delete=models.CASCADE)
    requested_date = models.DateField(default=None, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"Tour request by {self.client.email} for {self.hostel.hostelName}"
