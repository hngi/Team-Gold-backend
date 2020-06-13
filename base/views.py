from django.http import Http404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from . import serializers
from .serializers import (
    UserSerializer,
    PlanSerializer,
    SubscriptionSerializer,
    TransactionSerializer,
)

from .models import User, Plan, Subscription, Transaction


class UserViewSet(viewsets.ModelViewSet):
    """Handles Listing, Creating, Deleting and Updating users."""

    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()


class PlanViewSet(viewsets.ModelViewSet):
    """Handles Listing, creating, Deleting and Updating plans."""

    serializer_class = serializers.PlanSerializer
    queryset = Plan.objects.all()


class SubscriptionViewSet(viewsets.ModelViewSet):
    """Handles Listing, creating, Deleting and Updatingsubscriptions."""

    serializer_class = serializers.SubscriptionSerializer
    queryset = Subscription.objects.all()


class TransactionViewSet(viewsets.ModelViewSet):
    """Handles Listing, Creating, Deleting and Updating transactions."""

    serializer_class = serializers.TransactionSerializer
    queryset = Transaction.objects.all()
