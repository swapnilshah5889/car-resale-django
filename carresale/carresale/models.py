from django.db import models

class Car(models.Model):
    
    # Basic information about the car
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=20)
    mileage = models.PositiveIntegerField()

    # Details about the car's condition and features
    condition_choices = [
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    ]
    condition = models.CharField(max_length=10, choices=condition_choices)
    
    features = models.TextField(blank=True, null=True)

    # Seller information
    seller_name = models.CharField(max_length=100)
    seller_email = models.EmailField()
    seller_phone = models.CharField(max_length=15)

    # Price and sale status
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_sold = models.BooleanField(default=False)

    # Date the car was listed
    date_listed = models.DateTimeField(auto_now_add=True)

    # Photo of the car
    photo = models.ImageField(upload_to='car_photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
