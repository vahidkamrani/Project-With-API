from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from .serializers import ComplaintSerializer
from .models import Complaint


@api_view(['POST'])
def post_complaint(request):
    data = {
        "Name" : request.data["Name"],
        "ID_name" : request.data["ID_name"],
        "Receivingـunit" : request.data["Receivingـunit"],
        "Typeـservice" : request.data["Typeـservice"],
        "Userـtype" : request.data["Userـtype"],
        "obtain" : request.data["obtain"],
        "Phone_number" : request.data["Phone_number"],
        "Mobile_number" : request.data["Mobile_number"],
        "Address" : request.data["Address"],
        "ID_customer" : request.data["ID_customer"],
        "Reason_complaint" : request.data["Reason_complaint"],
        "Complaint_description" : request.data["Complaint_description"],
        "suggestion" : request.data["suggestion"]
    }
    ser_data = ComplaintSerializer(data=data)

    if ser_data.is_valid():
        Complaint(
            Name = ser_data.validated_data['Name'],
            ID_name = ser_data.validated_data['ID_name'],
            Phone_number = ser_data.validated_data['Phone_number'],
            Mobile_number = ser_data.validated_data['Mobile_number'],
            Address = ser_data.validated_data['Address'],
            ID_customer = ser_data.validated_data['ID_customer'],
            Receivingـunit = ser_data.validated_data['Receivingـunit'],
            Typeـservice = ser_data.validated_data['Typeـservice'],
            Userـtype = ser_data.validated_data['Userـtype'],
            obtain = ser_data.validated_data['obtain'],
            Reason_complaint = ser_data.validated_data['Reason_complaint'],
            Complaint_description = ser_data.validated_data['Complaint_description'],
            suggestion = ser_data.validated_data['suggestion'],
        )
        ser_data.save()
        return Response(ser_data.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_complaints(request):
    complaints = Complaint.objects.all()
    ser_data = ComplaintSerializer(complaints, many=True)
    return Response(ser_data.data, status=status.HTTP_200_OK)