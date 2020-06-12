from rest_framework import serializers
from .models import User, Plan, Subscription, Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "email",
            "created_at",
            "updated_at",
        )


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ("id", "name", "cost", "annual_discount")


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = (
            "id",
            "name",
            "user",
            "created_at",
            "updated_at",
        )


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            "id",
            "name",
            "subscription",
            "user",
            "plan",
            "created_at",
            "updated_at",
        )

        def create(self, validated_data):
            user = User.objects.get(pk=validated_data["user"])
            plan = Plan.objects.get(pk=validated_data["plan"])
            subscription = Subscription.objects.get(
                pk=validated_data["subscription"]
            )
            transaction = Transaction.objects.create(
                user=user, subscription=subscription, transaction=transaction
            )
            return transaction
