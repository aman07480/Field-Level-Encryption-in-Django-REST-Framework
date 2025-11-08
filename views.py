from rest_framework.generics import ListCreateAPIView
from .models import Customer
from .serializers import CustomerSerializer

class CustomerView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
