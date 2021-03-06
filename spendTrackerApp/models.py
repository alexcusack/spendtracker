from django.db import models
from django.utils import timezone
from django.db.models import Sum

# Create your models here.

class User(models.Model):
    phone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone_number

    def lookup_user(phoneNumber):
        user = User.objects.filter(phone_number = phoneNumber)
        return user if user else None


class Charge(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    vendor = models.CharField(max_length=200)
    amount = models.IntegerField()
    time_of_charge = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def save_new_charge(user, amount, vendor):
        new_charge = Charge(user_id = user, amount=amount, vendor=vendor, time_of_charge=timezone.now())
        return new_charge.save()

    def get_charges_since_start_of_week(user_id):
        sum = 0
        for charge in Charge.objects.raw(
            # we can't do a summation here because Django requires including the 
            # primary key in the query result when working with raw queries.
            """
            select id, amount
            from "spendTrackerApp_charge" 
            where date_trunc('week', time_of_charge - interval '8 hours') >= date_trunc('week', now() - interval '8 hours')
            and user_id_id = %s;
            """
        , [user_id]):
            sum += charge.amount
        return sum

    def get_charges_since_start_of_day(user_id): 
        sum = 0
        for charge in Charge.objects.raw(
            """
            select id, amount
            from "spendTrackerApp_charge" 
            where date_trunc('day', time_of_charge - interval '8 hours') >= date_trunc('day', now() - interval '8 hours')
            and user_id_id = %s;
            """
        , [user_id]):
            sum += charge.amount
        return sum






