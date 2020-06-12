from django.contrib import admin
from .models import User, Plan, Subscription, Transaction

# Register your models here.
admin.site.register(User)
admin.site.register(Plan)
admin.site.register(Subscription)
admin.site.register(Transaction)