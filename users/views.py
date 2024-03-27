from rest_framework import generics, filters
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend



from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer


# class UserAPIView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({'message': 'User created successfully'})
#         return Response(serializer.errors, status=400)


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    # filter_backends = [OrderingFilter, SearchFilter]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    # filter_backends = [DjangoFilterBackend, OrderingFilter]
    # filterset_fields = ('paid_course', 'paid_lesson', 'pay_method')
    # ordering_fields = ('payment_date',)
    ordering_fields = ['payment_date']
    search_fields = ['paid_course', 'paid_lesson', 'pay_method']

