from django.db.models.signals import post_save
from django.dispatch import receiver
from  .models import Product

@receiver(post_save, sender = Product)
def log_product_created(sender, instance, created, **kwargs):
    if created:
        print(f"[Signal] New product added: {instance.name} for ₹{instance.price}")