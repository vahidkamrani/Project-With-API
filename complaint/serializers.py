from rest_framework import serializers
from django.utils import timezone
from .models import Complaint


class ComplaintSerializer(serializers.ModelSerializer):
    Reason_complaint = serializers.ListField(max_length=4)
    class Meta:
        model = Complaint
        fields = '__all__'
        read_only_fields = ("created_at",)


    def create(self, validated_data):
        obj = super().create(validated_data)
        obj.created_at = timezone.now()
        obj.save()
        return obj

         