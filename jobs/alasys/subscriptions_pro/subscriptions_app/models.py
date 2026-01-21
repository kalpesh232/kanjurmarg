from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

# Create your models here.

User = get_user_model()

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=50)
    monthly_credit = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name} ({self.monthly_credit}/mo)"

class UserSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.SET_NULL, null=True)
    credits = models.IntegerField(default=0)
    next_renewal= models.DateField(null=True,blank=True)

    def save(self, *args, **kargs):
        # initialize next_renewal on first save if missing
        if not self.next_renewal :
            self.next_renewal = timezone.now().date() + timedelta(days=30)
            print("*"*50)
            print("self.next_renewal  : ", self.next_renewal )
        super().save(*args,**kargs)

    def ensure_renewed(self):
        """If renewal date passed, add monthly credits and set next_renewal."""
        today = timezone.now().date()
        if self.plan and today >= self.next_renewal :
            self.credits += self.plan.monthly_credit
            # simple 30-day window
            self.next_renewal = today + timedelta(days=30)
            self.save()

    def deduct(self, amount):
        """Try to deduct credits; returns True if success."""
        self.ensure_renewed()
        if self.credits > amount :
            self.credits -= amount
            self.save()
            return True
        return False
    
    def recharge(self,amount):
        self.credits += amount
        self.save()

    def __str__(self):
        return f"{self.user.username} - {self.plan}"

