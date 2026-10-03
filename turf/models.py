from django.db import models

# Create your models here.

class Turf(models.Model):

    turf_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    SPORTS_CHOICE = [
        ("football","football"),
        ("cricket","cricket"),
        ("badminton","badminton"),
        ("volleyball","volleyball")
    ]
    sport_type = models.CharField(max_length=200,choices=SPORTS_CHOICE)
    price = models.FloatField()
    time = models.TimeField()
    contact_number = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Bookings(models.Model):
    name = models.CharField(max_length=200)

    phone_number = models.CharField(max_length=15)

    turf_id = models.IntegerField()

    booking_date = models.DateTimeField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    total_amount = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)


    