from django.db import models
# models.py

class Title(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title_text

class Description(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    description_text = models.TextField()

    def __str__(self):
        return self.description_text
# Create your models here.

# models.py

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

class Property(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=4, decimal_places=2)
    sqft = models.IntegerField()
    amenities = models.TextField()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
