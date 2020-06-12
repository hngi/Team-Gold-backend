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
from . import models
from .models import User, Plan, Subscription, Transaction


class UserViewSet(viewsets.ModelViewSet):
    """Handles Listing users."""

    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()


class PlanViewSet(viewsets.ModelViewSet):
    """Handles Listing plans."""

    serializer_class = serializers.PlanSerializer
    queryset = models.Plan.objects.all()


class SubscriptionViewSet(viewsets.ModelViewSet):
    """Handles Listing subscriptions."""

    serializer_class = serializers.SubscriptionSerializer
    queryset = models.Subscription.objects.all()


class TransactionViewSet(viewsets.ModelViewSet):
    """Handles Listing transactions."""

    serializer_class = serializers.TransactionSerializer
    queryset = models.Transaction.objects.all()
