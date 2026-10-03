from rest_framework import serializers
from turf.models import Turf
from turf.models import Bookings

from django.utils import timezone

class TurfSerializer(serializers.ModelSerializer):

    class Meta :
        model = Turf
        fields = "__all__"
        read_only_fields = ["id"]


class BookingSerializer(serializers.ModelSerializer):

    class Meta :

        model =  Bookings

        fields = "__all__"

        read_only_fields = ["turf_id","total_amount","created_at"]

    def validate(self,validated_data):

        booking_date = validated_data.get("booking_date")
        turf_id = Bookings.objects.get(id=turf_id)
        end_time = Bookings.objects

        if booking_date < timezone.localdate():

            raise serializers.ValidationError(" booking date should not be in the past")

        if not turf_id.exists():

            raise serializers.ValidationError("turf does not exists")
        
        
        else:
            return validated_data

        



