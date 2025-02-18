# signals.py
from django.db.models.signals import Signal
from django.dispatch import receiver

# Define a signal
object_saved = Signal()

# Receiver function to handle the signal
@receiver(object_saved)
def handle_object_saved(sender, **kwargs):
    print("Object saved! Do something here.")