from .models import Certificate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CertificateSerializer
from .html_to_pdf import generate_certificate
from django.utils import timezone


@api_view(['POST'])
def get_certificate(request):
    data = request.data
    name = data.get('Name')
    course = str(data.get('Course'))
    current_datetime = timezone.now()
    todays_date = current_datetime.date()
    todays_date_str = todays_date.strftime('%Y-%m-%d')
    result = generate_certificate(name, course, todays_date_str)
    return Response({'result': result})
