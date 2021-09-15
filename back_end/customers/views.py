from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .serializers import (
    CustomerSerializer
)
from .models import Customer

class CustomerListCreate(ListCreateAPIView):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class CustomerUpdateDelete(RetrieveUpdateDestroyAPIView):

    lookup_url_kwarg = 'customer_pk'

    serializer_class = CustomerSerializer
    
    def get_queryset(self):
        return Customer.objects.filter(id=self.kwargs["customer_pk"])
