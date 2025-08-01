from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, Property, Booking, Payment, Review, Message
from .serializers import UserSerializer, PropertySerializer, BookingSerializer, PaymentSerializer, ReviewSerializer, MessageSerializer
from .permissions import IsHostOrAdmin, IsGuestOrAdmin, IsOwnerOrAdmin, IsAdminOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrReadOnly]


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated, IsHostOrAdmin]

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, IsGuestOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
