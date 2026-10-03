from django.shortcuts import render,get_object_or_404

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from turf.models import Turf
from turf.models import Bookings

from turf.serializers import TurfSerializer
from turf.serializers import BookingSerializer

from rest_framework import serializers


class TurfCreateListView(APIView):

    def get(self,request):

        qs = Turf.objects.all()
        serializer_instance = TurfSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data = request.data 
        serializer_instance = TurfSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class TurfRetrieveUpdateDeleteView(APIView):

    def get(self,request,pk):
        qs=get_object_or_404(Turf,id=pk)
        serializer_instance = TurfSerializer(qs)
        return Response(data=serializer_instance.data)

    def put(self,request,pk):
        form_data =  request.data
        turf_object = get_object_or_404(Turf,id=pk)
        serializer_instance = TurfSerializer(data=form_data,instance=turf_object)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk):
        Turf.objects.filter(id=pk).delete()
        return Response(data={"MESSAGE":"DELETING....."})


class BookingCreateListView(APIView):

    def get(self,request):

        qs = Bookings.objects.all()
        serializer_instance = BookingSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data = request.data
        serializer_instance = BookingSerializer(data=form_data)
        if serializer_instance.is_valid():

            turf_id = serializer_instance.validated_data("turf_id")
            booking_date=serializer_instance.validated_data("booking_date")
            start_time = serializer_instance.validated_data("start_time")
            end_time = serializer_instance.validated_data("end_time")
             # check turf exists
            
            # check turf alredy booked
            if Bookings.objects.filter(
                turf_id=turf_id,
                booking_date=booking_date,
                start_time=start_time,
                end_time=end_time).exists():

                 return Response(data={"message":"turf already booked..."})
            

            serializer_instance.save()
            return Response(data=serializer_instance.data)

        else:
            return Response(data=serializer_instance.errors)

        
            

            
            

    



