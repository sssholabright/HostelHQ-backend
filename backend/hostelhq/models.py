from django.db import models

class UserProfile(models.Model):
    # Assuming this is your user profile model
    uid = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    approvalStatus = models.CharField(max_length=20, blank=True, null=True)
    approvedAgent = models.CharField(max_length=20, blank=True, null=True)
    verified = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Record creation time
    
    def __str__(self):
        return self.name or self.email

class AgentListing(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Link to UserProfile
    hostel_id = models.CharField(max_length=500, blank=True, null=True)
    agent_id = models.CharField(max_length=500, blank=True, null=True)
    hostelName = models.CharField(max_length=200, blank=True, null=True)  # Name of the hostel
    address = models.CharField(max_length=200, blank=True, null=True)  # Address of the hostel
    amenities = models.CharField(max_length=200, blank=True, null=True)  # Amenities offered
    description = models.TextField(blank=True, null=True)  
    availability = models.CharField(max_length=20, blank=True, null=True)  # Availability status
    capacity = models.IntegerField(blank=True, null=True)  # Number of rooms available
    price = models.CharField(max_length=20, blank=True, null=True)  # Price per room
    created_at = models.DateTimeField(auto_now_add=True)  # Record creation time

    def __str__(self):
        return f"{self.hostelName} - {self.address}"

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.image}"

class TourRequests(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='client_requests')
    hostel = models.ForeignKey(AgentListing, on_delete=models.CASCADE)
    requested_date = models.DateField(default=None, blank=True, null=True)
    status = models.CharField(max_length=10, )

    def __str__(self):
        return f"Tour request by {self.client.email} for {self.hostel.hostelName}"
