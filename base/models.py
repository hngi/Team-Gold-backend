from django.db import models

# Create your models here.

# UserTable
class User(models.Model):
    """ User Model"""

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def ___str___(self):
        return self.name


# PlanTable
class Plan(models.Model):
    """ plan Model"""

    name = models.CharField(max_length=100)
    # type = models.CharField(max_length=100)
    cost = models.IntegerField()
    annual_discount = models.IntegerField()

    def ___str___(self):
        return self.name


# Subscription
class Subscription(models.Model):
    """ Subscription Model"""

    name = models.CharField(max_length=100)

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user"
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def ___str___(self):
        return self.name


# Transaction
class Transaction(models.Model):
    """ Transcation Model"""

    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transaction_user"
    )
    plan = models.ForeignKey(
        Plan, on_delete=models.CASCADE, related_name="plan"
    )
    subscription = models.ForeignKey(
        Subscription, on_delete=models.CASCADE, related_name="subscription"
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def ___str___(self):
        return self.name
